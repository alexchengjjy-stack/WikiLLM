---
title: "如何用Agent Skill创建技能以及技能包 - 飛書雲端文件"
source: "https://feicaiclub.feishu.cn/wiki/RZDGw7z1ViOskTkEK8WcAcjGnGd"
author:
published:
created: 2026-04-19
description:
tags:
  - "clippings"
---
木火数字科技

👑

AI Agent | 如何用Agent Skill创建技能以及技能包

最新修改時間為 01月 22日

附件不支援列印

![飛書文件 - 圖片](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/QQURbiptAoN0bMxHngAcY9sBnAS/?fallback_source=1&height=1280&mount_node_token=Iy7SdGPOOoJ4LaxrsQmcQmJbnQc&mount_point=docx_image&policy=equal&width=1280)

<iframe src="https://player.bilibili.com/player.html?autoplay=0&amp;bvid=1r3yzBWE85&amp;share_source=copy_web&amp;vd_source=1adb0321bdfa6d9eb5d1bf5665ffc381" allowfullscreen="" allow="encrypted-media;local-network-access *;" frameborder="0"></iframe>

Skill Creator - 快速创建 Claude 自定义技能的方案
这套方案主要解决一个问题：虽然 Claude 官方提供了 Skill Creator，但它生成的技能提示词往往过于冗长复杂。对于想要快速创建符合自己工作流程的技能来说，需要一个更精简、更高效的工具。
所以我们自己搭建了一个 Skill Creator Agent。它通过结构化的问答方式收集你的需求，然后自动生成完整的技能包。你只需要回答几个问题 - 技能是做什么的、什么时候用、需要什么输入输出 - 它就能生成标准的 SKILL.md 文件，必要时还会自动创建 Reference 参考文档、Python 脚本或使用示例。
它的判断机制基于需求复杂度。简单的工作流程只生成核心的 SKILL.md；如果涉及大量参考资料，会拆分出 REFERENCE.md；如果有确定性操作（比如数据转换、API 调用），会生成配套的 Python 脚本。生成前会先展示完整预览，确认无误后再写入文件，避免返工。
更关键的是，用这个方案可以批量生产技能。一旦建立了 Skill Creator，你就能快速把各种工作流程标准化：产品分析、代码审查、文档生成、设计规范...每个流程都能沉淀成可复用的 Skill。甚至可以让多个 Skills 协同工作，形成完整的开发流程。
这个方案适合需要频繁创建和维护自定义技能的场景。通过它可以把团队的专业经验快速转化为 Claude 可以执行的标准化能力，而不用每次都从零编写复杂的提示词。


---
核心功能模块
/需求收集
基于结构化问答而非自由描述，Skill Creator 会通过渐进式提问引导你明确技能需求。系统会依次询问技能名称、核心功能、触发场景、输入输出、执行流程等关键要素。通过识别回答的完整度，动态决定是否需要追问细节 - 如果描述过于笼统，会追问具体场景；如果涉及大量数据，会询问是否需要脚本。

/智能判断
当需求收集完成后，系统会自动判断需要生成哪些文件。简单的工作流程只生成 SKILL.md 和 README.md；如果有超过 1000 字的参考资料（API 文档、设计规范、数据模型），会拆分出 REFERENCE.md；如果包含确定性操作需求（数据转换、API 调用、文件处理），会生成配套的 Python 脚本；如果示例超过 3 个或单个示例超过 200 字，会创建独立的 EXAMPLES.md。

/规范生成
所有生成的文件都遵循 Agent Skills 官方标准：SKILL.md 必须大写，包含 YAML 头部（name ≤ 64 字符、description ≤ 1024 字符）和正文四个模块（技能说明、核心能力、执行流程、注意事项）。description 字段会自动组织成"功能描述 + 使用场景 + 触发关键词"的格式，确保 Claude 能准确识别何时调用该 Skill。

/质量把控
系统内置完整的质量标准和命名规范。文件夹使用小写字母加下划线（csv_converter），SKILL.md、README.md、EXAMPLES.md 全部大写，REFERENCE 文件格式为 REFERENCE_<NAME>.md。执行流程必须具体可操作，避免模糊描述；使用占位符而非固定内容保持灵活性；如果引用 Reference 文档，必须使用正确的相对路径。

注：Skill Creator 生成的技能质量很大程度上取决于你提供的信息质量。如果你对工作流程的理解不够清晰，或者没有提前梳理好关键的 know-how，生成的技能往往会流于表面，缺乏实际执行价值。建议在创建技能前，先明确核心步骤、关键决策点、常见问题的处理方式，这样生成的技能才能真正发挥作用。


---
在 Claude Code 中配置单个 Skill
请跟着视频中的教学并且按照以下步骤配置你的第一个 Skill，让 Claude Code 掌握专业的产品需求分析能力。配置完成后，你的项目结构应该是这样：
project/
├── .claude/
│   └── skills/
│       └── product_manager_expert/
│           └── SKILL.md            # 产品经理技能文件（必须创建）
└── ...

配置步骤：
1. 创建技能目录 - 在项目中创建 .claude/skills/product_manager_expert/ 目录结构
2. 创建技能文件 - 在该目录下创建 SKILL.md 文件（注意必须全大写）
3. 编写 YAML 头部 - 定义技能的 name 和 description，description 要包含功能说明和触发场景
4. 编写技能内容 - 按照标准结构填写技能说明、核心能力、执行流程、注意事项四个模块

---
name: skill_name
description: 技能功能描述。使用场景说明。触发关键词。
---

[技能说明]
    简要描述这个技能的能力和专业领域

[核心能力]
    - **能力1**：具体说明
    - **能力2**：具体说明
    - **能力3**：具体说明

[执行流程]
    第一步：步骤名称
        - 具体操作1
        - 具体操作2

    第二步：步骤名称
        - 具体操作1
        - 具体操作2

[注意事项]
    - 重要约束和规范
    - 质量标准
    - 边界条件

重要配置细节：
- 目录路径 必须严格按照 .claude/skills/<skill_name>/ 格式，否则 Claude 无法识别
- 文件名规范 SKILL.md 必须全大写，这是官方硬性要求，大小写错误会导致技能无法加载
- YAML 头部 name 不超过 64 字符，description 不超过 1024 字符，且 description 是 Claude 判断何时使用该技能的关键
- 执行流程 要具体可操作，每一步要清晰明确，避免"根据情况灵活处理"这类模糊描述
- 占位符使用 用 <项目名称> <目标用户> 这样的占位符而非固定内容，保持技能的通用性
- 文档引用 如果技能需要引用参考文档，使用相对路径 [参考文档](reference.md)

验证配置： 配置完成后，可以通过简单对话测试：告诉 Claude "我要开发一个灵活用工的 App"，Claude 应该会自动识别并调用 product_manager_expert 技能，开始进行需求分析并生成 PRD.md 文档。如果 Claude 没有自动调用，检查 SKILL.md 的 description 是否包含了足够的触发关键词。
这个配置是所有技能的基础模式。一旦掌握了单个 Skill 的创建方法，你就可以快速创建更多专业技能，或者进一步组合多个 Skills 形成完整的工作流。


---
在 Claude Code 中配置多个 Skill 并串联成工作流
当你需要完成一个完整的产品开发流程时，可以配置多个 Skills 协同工作。以产品开发为例，我们将产品经理、设计师、开发者三个 Skills 串联起来，形成从需求到代码的完整链路。配置完成后，你的项目结构应该是这样：
project/
├── .claude/
│   ├── CLAUDE.md                           # 主流程控制规则（必须创建）
│   └── skills/
│       ├── product_manager_expert/
│       │   └── SKILL.md                    # 产品经理技能
│       ├── designer_expert/
│       │   └── SKILL.md                    # 设计师技能
│       └── developer_expert/
│           └── SKILL.md                    # 开发者技能
├── PRD.md                                  # 产品需求文档（自动生成）
├── DESIGN_SPEC.md                          # 设计规范文档（自动生成）
└── ...                                     # 前端代码文件（自动生成）

配置步骤：
1. 创建技能目录 - 按照上述结构分别创建三个技能的目录和 SKILL.md 文件
2. 创建主控文件 - 在 .claude/ 目录下创建 CLAUDE.md 文件，定义工作流程和调度逻辑
3. 配置指令映射 - 在 CLAUDE.md 中定义 /PRD、/设计、/开发 等指令，映射到对应的 Skill
4. 设置文档传递 - 明确各阶段生成的文档如何传递给下一阶段（PRD.md → Designer → Developer）

重要配置细节：
- Skills 数量 按照同样的方法，你想添加几个 Skill 就添加几个。每个 Skill 独立配置在自己的目录下
- 串联方式 如果要形成工作流，强烈建议使用 CLAUDE.md 来串联。这样做最方便，流程清晰明确
- 自然对话串联 技术上你也可以不用 CLAUDE.md，纯靠自然对话来引导 Claude 依次调用各个 Skill。但这种方式只适合你自己用，因为只有你清楚完整的流程。如果要分享给团队或其他人，别人根本不知道该怎么操作、按什么顺序执行
- 指令映射 虽然 Skills 可以通过自然语言自动触发，但为了稳定性，建议在 CLAUDE.md 中使用明确的指令映射
- 文档传递 每个 Skill 生成的文档会自动保存，下一个 Skill 会通过读取这些文档来获取上下文
- 流程控制 CLAUDE.md 中的主 Agent 负责引导用户按正确顺序执行，确保流程连贯
- Skills 独立性 每个 Skill 应该保持独立，只负责自己的专业领域，通过主控文件来协调整体

验证配置： 配置完成后，启动 Claude Code 并描述你的产品想法。Claude 会引导你完成需求收集，然后提示输入 /PRD 生成产品文档。验证 PRD.md 生成成功后，输入 /设计 生成设计规范。最后输入 /开发 生成完整代码。整个流程应该是连贯的，每个阶段的输出都会被下一阶段正确读取和使用。
这种多 Skill 协作的方式特别适合需要跨职能配合的复杂任务。你可以根据实际需求调整 Skills 的数量和类型，比如增加"测试工程师"Skill 进行代码审查，或者"技术文档"Skill 生成 API 文档。关键是保持每个 Skill 的职责单一清晰，通过 CLAUDE.md 主控文件来协调整体流程，让工作流可以复用和分享。


---
Skill、Agent、Command 的区别
Skill 强调的是标准化和可复用，你创建一次后可以在任何地方反复使用，并且可以打包分享给团队。Agent 强调的是独立上下文和并行工作，它会在一个隔离的环境中完成任务，适合处理复杂的独立任务。Command 就像快捷键，手动触发，执行简单的即时操作。所以日常工作流程用 Skill，复杂独立任务用 Agent，临时简单操作用 Command。

[圖片]


---