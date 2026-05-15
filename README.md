# 2026 理工科 AI 就业风险矩阵

基于任务暴露分析的 STEM 专业入口风险评估，覆盖 11 个大类、100+ 子方向。

**核心判断：AI 不会按专业名淘汰人，它会重排入行路径——只做标准任务的人先被压缩，能承担系统和责任的人更有位置。**

## 👉 [在线阅读完整分析](https://georgehawkie-hash.github.io/ai-risk-analysis/stem_ai_job_risk_article.html)

也可以克隆仓库后双击 `stem_ai_job_risk_article.html` 在本地浏览器中查看。

## 四个时间窗口

| 决策场景 | 看什么时候 |
|---|---|
| 2026 高考选专业 | 看 2030 |
| 2026/2027 考研 | 看 2029 |
| 本科在读转向 | 看 2027-2028 |
| 读博/科研路线 | 看 2031+ |

## 覆盖专业

计算机/软件/数据/AI · 数学/统计/物理 · 电子/微电子/集成电路 · 电气/能源动力 · 自动化/机器人/智能制造 · 机械/仪器 · 土木/建筑/水利/测绘/交通/环境 · 材料/化学/化工/制药 · 生物/生物工程/生物医学工程 · 工业工程/管理科学/物流 · 交叉学科/新工科

## 风险等级

- 🔴 **高** — 入口任务高度数字化，已被 AI 明显压缩
- 🟠 **中高** — 大量入口任务可被加速，但仍需落地能力
- 🟡 **中** — 内部分化大，通用任务暴露但系统/现场更稳
- 🟢 **低** — 物理/现场/安全/法规约束强，直接替代慢
- 🔵 **机会** — 需求可能扩张，但低端演示仍有风险

## 方法

借鉴 Anthropic 的 observed exposure 方法：先拆解职业任务，再看真实 AI 使用数据，而非直接预测"AI 会不会替代某专业"。

## 数据来源

主要来源包括：Anthropic Economic Index、Stanford HAI AI Index、METR、WEF Future of Jobs、BLS 职业数据、教育部本科专业目录、国务院/工信部/国家能源局政策文件、IFR 世界机器人报告等。完整列表见文章末尾。

## 项目结构

```
├── stem_ai_job_risk_article.html   # 完整文章（可直接浏览）
├── stem_ai_job_risk_article.md     # Markdown 源文本
├── LICENSE                         # 版权声明
├── robots.txt                      # AI 爬虫屏蔽规则
└── data/
    ├── major_risk_database.json    # 结构化风险数据库
    ├── public_ai_impact_sources.json # 公开情报来源
    ├── claude_independent_review.md  # 独立审核记录
    └── claude_*_subfield_review.md   # 各专业子方向审核
```

## 版权

© 2026 Yixu Yao. 保留所有权利。

未经许可，禁止全文转载、商业使用、改编发布、批量抓取或用于训练机器学习模型。允许在非商业讨论、教学或评论中引用少量内容，须注明来源。详见 [LICENSE](LICENSE)。
