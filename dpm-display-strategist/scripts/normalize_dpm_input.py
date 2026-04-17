#!/usr/bin/env python3
"""Normalize DPM intake files into a lightweight JSON structure.

The script is intentionally conservative: it extracts text, tables, field IDs,
answers, and obvious missing critical areas. It does not score clients or make
relationship judgments.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import zipfile
from html import unescape
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


FIELD_RE = re.compile(r"\b([BPLATMGZCS]\d{2})\b", re.IGNORECASE)
BLANKS = {"", " ", "　", "-", "—", "无", "暂无", "不详", "未填写", "N/A", "n/a"}


def clean(value: Any) -> str:
    if value is None:
        return ""
    text = unescape(str(value))
    text = re.sub(r"\s+", " ", text.replace("\u3000", " ")).strip()
    return text


def is_blank(value: str) -> bool:
    return clean(value) in BLANKS


def read_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md", ".markdown"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    if suffix == ".csv":
        return read_csv(path)
    if suffix == ".json":
        return json.dumps(json.loads(path.read_text(encoding="utf-8")), ensure_ascii=False, indent=2)
    if suffix == ".docx":
        return read_docx(path)
    if suffix in {".xlsx", ".xlsm"}:
        return read_xlsx(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def read_csv(path: Path) -> str:
    rows = []
    with path.open("r", encoding="utf-8-sig", errors="ignore", newline="") as fh:
        for row in csv.reader(fh):
            rows.append(" | ".join(clean(cell) for cell in row))
    return "\n".join(rows)


def read_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    lines = []
    for paragraph in root.findall(".//w:p", ns):
        texts = [node.text or "" for node in paragraph.findall(".//w:t", ns)]
        line = clean("".join(texts))
        if line:
            lines.append(line)
    return "\n".join(lines)


def read_xlsx(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        shared = read_shared_strings(zf)
        sheet_names = sorted(name for name in zf.namelist() if name.startswith("xl/worksheets/sheet"))
        lines = []
        for sheet_name in sheet_names:
            lines.append(f"# {sheet_name}")
            root = ET.fromstring(zf.read(sheet_name))
            ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            for row in root.findall(".//a:row", ns):
                cells = []
                for cell in row.findall("a:c", ns):
                    value = cell.find("a:v", ns)
                    raw = value.text if value is not None else ""
                    if cell.attrib.get("t") == "s" and raw.isdigit():
                        raw = shared[int(raw)] if int(raw) < len(shared) else raw
                    cells.append(clean(raw))
                if any(cells):
                    lines.append(" | ".join(cells))
        return "\n".join(lines)


def read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    values = []
    for si in root.findall(".//a:si", ns):
        parts = [node.text or "" for node in si.findall(".//a:t", ns)]
        values.append(clean("".join(parts)))
    return values


def split_table_row(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    return [clean(part) for part in stripped.split("|")]


def extract_fields(text: str) -> dict[str, dict[str, str]]:
    fields: dict[str, dict[str, str]] = {}
    for lineno, line in enumerate(text.splitlines(), 1):
        if not FIELD_RE.search(line):
            continue
        field_id = FIELD_RE.search(line).group(1).upper()  # type: ignore[union-attr]
        cells = split_table_row(line) if "|" in line else re.split(r"[:：]\s*", line, maxsplit=1)
        cells = [clean(cell) for cell in cells if clean(cell)]
        answer = ""
        question = ""
        if len(cells) >= 4:
            question = cells[1]
            answer = cells[-1]
        elif len(cells) == 3:
            question = cells[1]
            answer = cells[2]
        elif len(cells) == 2:
            question = cells[0].replace(field_id, "").strip()
            answer = cells[1]
        else:
            question = line
        if answer in {"用户填写", "填写", "用户答案"}:
            answer = ""
        fields[field_id] = {
            "question": question,
            "answer": answer,
            "source": f"line:{lineno}",
        }
    return fields


def any_answer(fields: dict[str, dict[str, str]], ids: list[str]) -> bool:
    return any(not is_blank(fields.get(field_id, {}).get("answer", "")) for field_id in ids)


def missing_critical(fields: dict[str, dict[str, str]]) -> list[str]:
    checks = [
        ("basic_situation", ["B01", "B03", "B04", "B08"]),
        ("relationship_goal", ["B14", "G01", "G02"]),
        ("true_advantages", [f"A{i:02d}" for i in range(1, 9)] + ["P09"]),
        ("target_partner", ["T01", "T02", "T05", "T15"]),
        ("dealbreakers", ["T12", "G05", "G10", "G15"]),
        ("display_materials", ["C01", "C03", "C04", "C06"]),
    ]
    return [name for name, ids in checks if not any_answer(fields, ids)]


def build_client_meta(fields: dict[str, dict[str, str]]) -> dict[str, str]:
    def ans(field_id: str) -> str:
        return fields.get(field_id, {}).get("answer", "")

    return {
        "name": ans("B01"),
        "age": ans("B03"),
        "city": ans("B04"),
        "relationship_goal": ans("B14") or ans("G01"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize DPM intake input into JSON.")
    parser.add_argument("input", help="Path to .md/.txt/.csv/.json/.docx/.xlsx file, or '-' for stdin")
    parser.add_argument("--out", help="Optional output JSON path")
    args = parser.parse_args()

    if args.input == "-":
        text = sys.stdin.read()
        source = "stdin"
    else:
        path = Path(args.input).expanduser()
        text = read_text(path)
        source = str(path)

    fields = extract_fields(text)
    result = {
        "client_meta": build_client_meta(fields),
        "raw_fields": fields,
        "normalized_fields": {},
        "missing_critical_fields": missing_critical(fields),
        "contradictions": [],
        "private_model": {},
        "source": source,
        "stats": {
            "characters": len(text),
            "field_count": len(fields),
            "answered_field_count": sum(1 for item in fields.values() if not is_blank(item.get("answer", ""))),
        },
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
