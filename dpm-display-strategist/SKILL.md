---
name: dpm-display-strategist
description: 读取DPM 2.4相亲展示面客户资料并生成客户可读的相亲平台完整展示面资料包。Use when Codex needs to process a user's uploaded DPM填空表、飞书文档链接、Word/Excel/CSV/Markdown/plain-text客户资料, normalize the information, ask only critical follow-up questions if needed, privately model真实优势、目标伴侣、硬边界、差异化和展示可行性, then output a non-scoring, authenticity-safe dating profile package focused on相亲平台基础资料展示、自我介绍、优势爱好表达、对另一半期许、头像照片组、筛选表达和互动话术.
---

# DPM 展示面策略师

## Goal

Turn a filled DPM client intake file into a client-facing dating platform profile package. Keep the scope narrow: first version only covers相亲平台展示面, not朋友圈、小红书、短视频完整方案.

## Non-Negotiables

- Do not show DPM scores, formulas, or backend variable names in the client-facing report.
- Do not invent facts, inflate status, or package the client as someone they cannot sustain.
- Use MBTI and zodiac only as auxiliary language for communication preference and relationship气质; never use them as hard matching criteria.
- Prefer concrete evidence and lived examples over self-claims like “真诚”“靠谱”“情绪稳定”.
- If key information is missing, ask at most 3-5 critical follow-up questions, then generate with explicit information boundaries.

## Workflow

1. **Read input**
   - For local files, run `scripts/normalize_dpm_input.py <file>` when useful.
   - For Feishu links, first read/export the document with available Feishu tools, then pass the resulting Markdown/text/file to the normalizer if helpful.
   - If parsing fails, ask the user to upload Word/Excel/Markdown or paste the filled content.

2. **Normalize**
   - Produce or mentally maintain this working shape:

```json
{
  "client_meta": {},
  "raw_fields": {},
  "normalized_fields": {},
  "missing_critical_fields": [],
  "contradictions": [],
  "private_model": {}
}
```

3. **Check completeness**
   - Load `references/input-schema.md`.
   - Confirm enough information exists for: basic situation, relationship goal, real advantages, target partner, dealbreakers, display materials.
   - If not, load `references/missing-info-questions.md` and ask only the highest-impact 3-5 questions.

4. **Privately model**
   - Load `references/dpm-model-rubric.md`.
   - Privately assess true advantages, target fit, hard/soft boundaries, differentiation, content landing ability, authenticity, and sustainability.
   - Keep all scores hidden. Translate internal judgments into plain-language strategy.

5. **Generate the report**
   - Load `references/report-template.md`, `references/dating-platform-playbook.md`, and `references/copy-style-adaptation.md`.
   - Output the 8-section client-facing profile package.
   - Keep tone warm, specific, practical, and free of “你条件很好/很差” style ranking.

## Input Handling Rules

- Standard DPM V0.2 fields use prefixes: `B`基础信息, `P`性格与关系, `L`生活方式, `A`真实优势, `T`理想伴侣, `M`MBTI, `Z`星座, `G`关系边界, `C`展示素材, `S`补充信息.
- Non-standard files are acceptable. Map by meaning, not only field IDs.
- Treat blank tables as intake templates, not client data. Ask the user to upload the filled version.
- If uploaded content contains private details, do not repeat unnecessary sensitive facts in the report; use generalized language.

## Follow-Up Rules

Ask follow-ups only when missing data would materially change the profile strategy. Prioritize:

1. What kind of relationship and marriage timeline the client actually wants.
2. Who the client most wants to attract.
3. What the client will not accept.
4. Concrete examples proving the client’s claimed strengths.
5. What materials can be shown publicly on the dating platform.

If the user does not answer follow-ups, proceed with assumptions and include a short “信息边界” note.

## Output Rules

- Use the exact 8 sections from `references/report-template.md`.
- Include complete dating profile materials: 基础资料展示、自我介绍、优势表达、爱好表达、对另一半的期许、筛选表达、opening/reply scripts.
- Make usable copy sound like a real person. Choose a communication archetype from the client’s personality and参考类似类型公众人物的表达习惯 only as tone inspiration; never impersonate or claim to be that person.
- Separate “适合公开写进资料” from “适合私聊后表达”.
- Give photo guidance as a 6-9 photo set, not vague advice like “多放生活照”.
- Do not output a 7-day implementation checklist.

## Quality Bar

The final report should help the client know:

- 我应该被理解成什么样的人。
- 我最该展示哪些真实优势。
- 我适合吸引谁，也该筛掉谁。
- 我的相亲平台基础资料、自我介绍、头像、照片、标签和话术具体怎么做。
- 哪些表达会过度包装、带来错配或不可持续。
