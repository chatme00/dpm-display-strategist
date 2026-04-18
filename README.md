# DPM 相亲展示面策略师

`dpm-display-strategist` 是一个面向中文相亲咨询场景的 Codex Skill。

它可以读取用户填写好的 DPM 相亲展示面信息采集表，自动梳理客户的真实优势、目标伴侣画像、关系边界与可展示素材，最后输出一份客户可以直接使用的相亲平台完整展示面资料包。

这个 Skill 不是给客户“打分”，也不是把客户包装成另一个人。它的目标是：

- 把客户真实但模糊的自我介绍，转成清晰、有记忆点的展示面
- 把“我有什么优势”转成可被看见、可被相信的资料表达
- 把“我想找什么人”转成温和但有效的筛选信号
- 输出头像、照片组、自我介绍、标签、择偶期许和互动话术
- 让文案更像真人，而不是咨询报告或模板套话

## 适合谁使用

- 相亲顾问、婚恋咨询师、个人形象/展示面咨询师
- 想帮客户优化相亲平台资料的人
- 需要把客户信息表转成展示面方案的内容工作者
- 想系统化搭建相亲资料页的人

## 能输出什么

Skill 默认输出一份客户可读的相亲平台展示面资料包，包含：

1. 展示面核心定位
2. 基础资料展示
3. 自我介绍完整文案
4. 真实优势提炼
5. 目标伴侣画像与筛选边界
6. 相亲平台照片与版面设计
7. 可直接使用的参考文案
8. 互动承接话术与真实性提醒

## 案例示例

下面是一个虚拟客户案例，用来展示从输入表到输出方案的完整效果。

### 案例：98 年内向男生陈亦泽

输入文件：

- [98 年内向男生虚拟资料.xlsx](examples/chen-yize/input.xlsx)

输出文件：

- [DPM_陈亦泽_相亲平台展示面方案.md](examples/chen-yize/output.md)

输出片段：

```markdown
一句话定位：一个在杭州生活稳定、慢热但认真、用行动表达在意的男生。

气质关键词建议：慢热、稳定、踏实、低调、有生活秩序。

更适合被理解成：不是很会在一开始制造热闹气氛的人，但不是冷漠；他的认真更多体现在准时、守信、记得实际需要、愿意一起把日子过稳。
```

自我介绍片段：

```markdown
我现在在杭州滨江工作，做新能源设备运维/测试相关，生活节奏比较固定。平时不是特别外向的人，刚认识会慢一点，但熟了以后会更自然。

工作日基本是上班、吃饭、休息，偶尔去健身房；周末会睡个懒觉、打扫房间、看电影，或者和朋友简单吃个饭。我不太擅长一开始就聊得很热闹，但会把在意放在具体事情上，比如接送、帮忙处理问题、记得对方需要什么。
```

这个案例展示了 Skill 的核心能力：不把内向包装成外向，而是把“慢热、稳定、行动型照顾”翻译成更容易被目标对象理解和接受的展示面表达。

## 仓库结构

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

examples/
└── chen-yize/
    ├── input.xlsx
    └── output.md
```

## 安装方式

### 使用 `npx skills`

适用于支持 open skills CLI 的 Agent：

```bash
npx skills add https://github.com/chatme00/dpm-display-strategist --skill dpm-display-strategist
```

Codex 全局安装：

```bash
npx skills add https://github.com/chatme00/dpm-display-strategist \
  --skill dpm-display-strategist \
  --agent codex \
  --global
```

### 使用 Codex 内置 skill installer

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo chatme00/dpm-display-strategist \
  --path dpm-display-strategist
```

安装后请重启 Codex，让新 skill 生效。

## 使用方式

先让客户填写模板：

- [DPM 相亲展示面客户信息采集表.xlsx](templates/DPM%20相亲展示面客户信息采集表.xlsx)

然后在 Codex 中使用：

```text
使用 $dpm-display-strategist 读取这份客户资料，补问关键缺失项，并生成相亲平台完整展示面资料包。
```

支持的输入形式：

- 飞书文档导出的 Markdown / 文本
- Word 文档
- Excel / CSV 表格
- Markdown 文件
- 纯文本客户资料

## 设计原则

- 不向客户展示后台分数
- 不虚构客户的优势、经历、收入或性格
- MBTI 和星座只作为表达风格辅助，不作为硬匹配依据
- 文案要像真人会写的话，不像咨询报告
- 首版聚焦相亲平台，不展开朋友圈、小红书、短视频完整方案
- 不提交真实客户资料到公开仓库

## Release 下载

可以在 [v0.1.0 Release](https://github.com/chatme00/dpm-display-strategist/releases/tag/v0.1.0) 下载空白信息采集表。

## License

MIT
