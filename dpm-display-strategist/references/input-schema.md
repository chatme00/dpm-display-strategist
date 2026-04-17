# DPM V0.2 Input Schema

Use this reference when checking uploaded DPM client资料 or mapping non-standard files into DPM fields.

## Sections

- Field groups and critical fields
- Standard V0.2 question map
- Alias mapping for non-standard files
- Normalized working JSON

## Field Groups

| Prefix | Group | Purpose |
|---|---|---|
| B | 基础信息 | Basic market context: age, city, work, relationship goal, family/marriage background |
| P | 性格与关系风格 | Personality, emotional pattern, conflict style, intimacy needs |
| L | 生活方式 | Daily rhythm, social style, money/life habits, material that can be shown |
| A | 真实优势申报 | Claimed strengths and how they appear in real life |
| T | 理想伴侣画像 | Desired partner, relationship expectations, must-haves and dealbreakers |
| M | MBTI补充 | Communication and personality preference signals only |
| Z | 星座补充 | Emotional narrative and relationship气质 signals only |
| G | 关系边界与匹配 | Marriage, childbirth, city, money, family, emotional and social boundaries |
| C | 展示面素材与边界 | Public/private display materials and profile goals |
| S | 补充信息 | Past dating issues and extra context |

## Critical Fields

The report can be generated when these six information areas are reasonably covered:

1. **Basic situation**: name/call sign, age, city, work/life context.
2. **Relationship goal**: why dating now, marriage timeline, relationship pace.
3. **True advantages**: at least 3 claimed strengths with concrete behavior or recognition.
4. **Target partner**: ideal partner description, desired traits, relationship expectations.
5. **Dealbreakers**: cannot-accept conditions, city/marriage/child/family boundaries.
6. **Display materials**: willingness to show face/photos, usable photos/life scenes, privacy boundaries.

If three or more critical areas are missing, ask follow-up questions before generating.

## Standard V0.2 Question Map

### Basic B

- B01 report name; B02 gender; B03 age; B04 current city; B05 city plan; B06 height; B07 education; B08 job; B09 work status; B10 economic status; B11 living status; B12 relationship/marriage history; B13 children; B14 reason for dating now; B15 attitude to long-distance.

### Personality and Relationship P

- P01 self-description; P02 others' evaluation; P03 active/slow in relationships; P04 expression of care; P05 stress/emotion handling; P06 desired emotional response; P07 conflict reaction; P08 conflict case; P09 relationship value; P10 improvement area; P11 needs for security/companionship/freedom; P12 decision style.

### Lifestyle L

- L01 daily rhythm; L02 weekend activities; L03 social style; L04 consumption view; L05 housing/savings/shared finance; L06 long-term habits; L07 life-quality details; L08 preferred dates; L09 disliked interaction style; L10 willingness to show face; L11 sustainable content material; L12 first-impression气质.

### Advantages A

- A01-A08 advantage rows: strength, concrete manifestation, who recognized it, who it attracts, willingness to display.

### Target Partner T

- T01 ideal partner paragraph; T02 stable traits; T03 realistic conditions; T04 lifestyle; T05 relationship management; T06 relationship pace; T07 marriage/children; T08 city/settlement; T09 family boundary; T10 money/life plan; T11 bonus traits; T12 unacceptable cases; T13 past attraction; T14 past mismatch; T15 most desired target.

### MBTI/Zodiac M/Z

- M01 own MBTI; M02 resemblance; M03 preferred MBTI/personality; M04 reason.
- Z01 own zodiac; Z02 preferred zodiac/temperament; Z03 reason.

### Boundaries G

- G01 own marriage timing; G02 minimum partner marriage intention; G03 own child plan; G04 child-plan bottom line; G05 city non-negotiables; G06 long-distance range; G07 income/economic responsibility; G08 consumption concern; G09 family boundaries; G10 emotional/communication no-goes; G11 social/opposite-sex boundary; G12 lifestyle minimum similarity; G13 career/family balance; G14 negotiable but negative items; G15 one-vote vetoes; G16 decision priority when conditions partially mismatch.

### Display C and Supplement S

- C01 desired displayed self; C02 feared misunderstanding; C03 available photos/videos/life materials; C04 private info not public; C05 info for later private chat; C06 dating-platform content; C07 social media content; C08 Xiaohongshu/short-video willingness; C09 memorable sentence; C10 contrast/memory point; C11 dissatisfaction with past profile; C12 core problem to solve.
- S01 repeated dating problem; S02 people currently attracted; S03 people truly desired; S04 people to screen out; S05 must-know context.

## Alias Mapping for Non-Standard Files

Map by semantic intent:

- “自我介绍 / 我是谁 / 个人情况” -> B + P.
- “择偶标准 / 理想对象 / 想找的人” -> T.
- “不能接受 / 底线 / 雷区” -> G/T12.
- “优势 / 亮点 / 被朋友评价” -> A/P02/P09.
- “照片素材 / 可展示内容 / 主页资料” -> C.
- “MBTI / 星座 / 性格类型” -> M/Z.

## Normalized Working JSON

Use this shape internally:

```json
{
  "client_meta": {
    "name": "",
    "age": "",
    "city": "",
    "relationship_goal": ""
  },
  "raw_fields": {
    "B01": {"question": "", "answer": "", "source": ""}
  },
  "normalized_fields": {
    "basic": {},
    "personality": {},
    "lifestyle": {},
    "advantages": [],
    "target_partner": {},
    "boundaries": {},
    "display_materials": {}
  },
  "missing_critical_fields": [],
  "contradictions": [],
  "private_model": {}
}
```
