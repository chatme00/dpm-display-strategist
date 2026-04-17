# DPM Display Strategist

`dpm-display-strategist` is a Codex skill for turning a filled DPM dating-profile intake form into a client-facing dating platform profile package.

It reads DPM client materials, normalizes the answers, asks only critical follow-up questions when needed, privately reasons through the DPM 2.4 model, and outputs a warm, practical, non-scoring dating profile package focused on:

- Basic profile fields
- Self-introduction copy
- True strengths, hobbies, and relationship expectations
- Target partner positioning and screening boundaries
- Avatar and 6-9 photo set guidance
- Dating-platform bio variants
- Opening, reply, and low-pressure screening scripts

The skill is designed for Chinese-language dating consulting workflows and keeps backend scores hidden from the client-facing report.

## Repository Structure

```text
dpm-display-strategist/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── copy-style-adaptation.md
│   ├── dating-platform-playbook.md
│   ├── dpm-model-rubric.md
│   ├── input-schema.md
│   ├── missing-info-questions.md
│   └── report-template.md
└── scripts/
    └── normalize_dpm_input.py

templates/
└── DPM 相亲展示面客户信息采集表.xlsx
```

## Install

After this repository is on GitHub, install the skill with the Codex skill installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path dpm-display-strategist
```

Then restart Codex so the new skill is picked up.

## Usage

Use the skill with a filled DPM intake file:

```text
使用 $dpm-display-strategist 读取这份客户资料，补问关键缺失项，并生成相亲平台完整展示面资料包。
```

Supported input styles:

- Feishu document content exported or pasted as Markdown/text
- Word documents
- Excel/CSV files
- Markdown files
- Plain text client notes

The included spreadsheet under `templates/` is an intake template. Do not commit filled client forms or private customer data to a public repository.

## Design Principles

- Do not expose DPM backend scores to clients.
- Do not fabricate achievements, status, or personality traits.
- Use MBTI and zodiac only as auxiliary expression signals, not hard matching rules.
- Make copy sound like a real person, not a consultant report.
- Keep the first version focused on dating platforms rather than social media or short-video platforms.

## License

MIT
