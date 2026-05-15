# math_statistics_physics subfields 独立审查意见

---

## 一、总体判断

数据库在"三族同屏"框架上方向正确，12 个子方向的分类骨架基本合理，风险评级的颗粒度优于常见的"某专业会被 AI 替代"式简化论断。但仍存在若干**必须修改**的结构性问题：量化/精算混装、光电/半导体/量子/材料打包过粗、公职出口整体缺失独立覆盖、与计算机类 data_analysis_bi 的同名重复未做交叉引用。整体结论：**修改后可作第一版样板，但不能以当前状态直接发布。**

---

## 二、必须修改的问题

### 2.1 金融数学/量化/风控/精算 混装（id: financial_math_quant_risk_actuarial）

这是 12 个子方向中**分类问题最严重的一个**。量化交易和精算保险是两条完全不同的职业路径：
- **量化**：买方/卖方量化研究，高度竞争，学历门槛极高（头部机构只要顶尖硕博），受市场周期影响大，无强制资质考试。
- **精算**：保险/养老金/风险管理，有独立的准精算师/精算师考试体系（SOA/CAS/中精），路径长但制度壁垒明确，岗位总量有限但替代速度较慢。

当前将它们合并在 medium_high 评级下会**同时误导两类读者**：量化方向的学生可能低估竞争烈度，精算方向的学生可能高估 AI 风险。

**修改方案**：拆成两个独立的子方向，分别评级——量化可保留 medium_high，精算可评为 medium。

### 2.2 光电/半导体/量子/材料物理 打包过粗且 opportunity 信号过强（id: optoelectronics_semiconductor_quantum_materials_physics）

四个方向的产业成熟度差距巨大：
- **半导体**：成熟产业，有真实招聘，但周期性强
- **光电**：细分领域多，部分成熟（显示、光通信），部分前沿
- **量子**：2027-2031 窗口内岗位总量极有限，更适合 PhD 路线
- **材料物理**：范围太广，从电池到超导，就业出口分散

当前标为 "opportunity" 容易让家长/学生理解为"这是好方向"，但量子方面本科/硕士阶段真实岗位极少，可能造成误导。coreJudgment 中"高机会方向"的措辞也过于肯定。

**修改方案**：至少拆成"半导体/光电物理"（opportunity 保留但加保守备注）和"量子/前沿材料物理"（降为 medium_high 或 medium，强调仅适合 PhD 路线且有极高不确定性）。evidenceGaps 也已承认"后续应再拆成二级方向"。

### 2.3 缺少公职/事业单位独立出口覆盖

数学类、统计学类学生在中国大陆通过公务员考试、事业单位招聘进入体制是重要出口（税务、统计、发改、审计、人民银行/金融监管等）。当前：
- `statistics_causal_inference_experiment_design` 仅在 entryRoles 中提及"统计局/事业单位数据岗"
- 没有独立的公职出口子方向
- 数学类学生的考公路径完全没有体现

这导致"非技术出口"覆盖不完整。公职岗位的 AI 风险机制与企业岗位完全不同：制度壁垒（编制考试）、流程约束、政策解释责任构成主要护城河，而非技术门槛。

**修改方案**：在数学类或统计学类下增加一个"公职/事业单位数理岗"子方向，或在两个教育子方向中增加对考公路径的交叉引用和独立 timeWindowNotes。

### 2.4 跨族同名条目 data_analysis_bi 未做区分

`data_analysis_bi_math_stats`（统计学类下）与计算机类下的 `data_analysis_bi_lowcode_reporting` 几乎完全重名，whyRisky/whyResilient/entryTasksAtRisk 高度相似。如果网页端三族同屏，读者会困惑"为什么同样内容出现两次"。

**修改方案**：统计学类下的 data_analysis_bi 应重命名为"统计向数据分析/BI"或在 coreJudgment 中明确说明与计算机类同名条目的差异（统计类学生应更强调实验设计、抽样、因果识别等统计专属能力，而非仅工具操作）。

---

## 三、建议修改的问题

### 3.1 纯数学教育出口的教培政策风险覆盖不足

`math_education_tutoring_exam_prep` 和 `physics_education_science_communication_tutoring` 的 whyRisky 主要聚焦 AI 技术替代，但中国大陆教培行业受"双减"政策冲击是**更强烈且更直接的变量**。当前仅在 evidenceGaps 中一笔带过"教培政策"，应进入 whyRisky。

### 3.2 实验物理的自动实验平台风险可能被低估

`experimental_physics_instrumentation_measurement` 的 counterarguments 仅写"自动实验平台会减少部分重复实验工作"，但 self-driving labs 在材料/化学领域已开始24/7自主实验+决策闭环。物理学中高通量测量和自动化的趋势值得在 whyRisky 中明确提及，而非仅放在 counterarguments。

### 3.3 理论/计算物理的"算法转岗"不应出现在 entryRoles

`theoretical_computational_physics` 的 entryRoles 包含"算法转岗"，这不是一个岗位名称，与同文件其他 entryRoles 的风格不一致。应替换为"算法工程师（转岗路径）"或直接删除。

### 3.4 运筹优化应提及与工业工程类交叉

`operations_research_industrial_optimization` 放在数学类下合理，但与 industrial_engineering 大类存在交叉竞争（工业工程学生也争运筹岗位）。可在 whyRisky 或 evidenceGaps 中加一句交叉竞争提示。

### 3.5 生物统计 entryRoles 的小问题

`biostatistics_pharma_statistics` 的 entryRoles 中"CRO 统计助理"在国内招聘中更常见的表述是"统计程序员"（Statistical Programmer）或"SAS 程序员"，建议调整以贴近实际招聘用语。

### 3.6 数学类缺少"信息与计算科学"出口映射

中国大陆"信息与计算科学"专业名义上属数学类，实际大量毕业生走向软件开发/算法。这个出口在纯数学和应用数学之间形成了灰色地带，当前未在 subfields 中有效覆盖。可在 pure_theoretical_mathematics 或 applied_math_scientific_computing 的 entryRoles/counterarguments 中增加对此类学生的提示。

---

## 四、评级调整建议表

| 子方向 ID | 当前评级 | 建议评级 | 调整理由 |
|---|---|---|---|
| financial_math_quant_risk_actuarial（量化部分） | medium_high | medium_high（维持） | 竞争烈度高但AI直接替代有限，评级合理 |
| financial_math_quant_risk_actuarial（精算部分） | medium_high | **medium** | 考试资质壁垒+制度约束，替代速度更慢，应拆出单独评级 |
| optoelectronics_semiconductor_quantum_materials_physics（半导体/光电部分） | opportunity | opportunity（维持，加保守备注） | 产业需求真实，但需注明周期风险和进入门槛 |
| optoelectronics_semiconductor_quantum_materials_physics（量子/前沿材料部分） | opportunity | **medium_high** | 2027-2031窗口内岗位总量极有限，opportunity信号过强 |
| experimental_physics_instrumentation_measurement | medium | medium（维持） | 评级合理，但whyRisky需补充自动实验平台内容 |
| math_education_tutoring_exam_prep | medium | medium（维持） | 评级合理，但whyRisky需补充政策风险 |
| physics_education_science_communication_tutoring | medium | medium（维持） | 同上 |
| 新增：公职/事业单位数理岗 | 无 | **medium**（新建） | 编制制度壁垒+政策解释责任+考试筛选，AI替代慢但岗位受招录政策影响 |
| data_analysis_bi_math_stats | high | high（维持） | 评级正确，需与计算机类同名条目做区分说明 |
| pure_theoretical_mathematics | medium_high | medium_high（维持） | 就业窄+升学叙事被AI增强，评级正确 |
| applied_math_scientific_computing | medium_high | medium_high（维持） | 需绑定工程场景的判断准确 |
| operations_research_industrial_optimization | medium_high | medium_high（维持） | 需落地行业闭环的判断准确 |
| statistics_causal_inference_experiment_design | medium | medium（维持） | 因果/实验设计护城河判断合理 |
| biostatistics_pharma_statistics | medium | medium（维持） | 临床试验合规约束判断合理，评级适当 |
| theoretical_computational_physics | medium_high | medium_high（维持） | 学术岗位有限+转岗竞争，评级合理 |

---

## 五、可以保留的判断

以下判断经过审查，分析链条完整、措辞适当，可保留：

1. **pure_theoretical_mathematics 的 coreJudgment**："抽象能力稀缺，但本科/硕士层面的解题、证明整理和升学叙事会被 AI 快速增强"——准确区分了研究价值和本科就业风险。

2. **operations_research_industrial_optimization 的 whyResilient**："真实优化需要处理脏数据、约束冲突、组织流程、异常工况和业务执行"——抓住了运筹落地的核心壁垒，表述务实。

3. **statistics_causal_inference_experiment_design 的 whyResilient**："政府统计、事业单位数据岗和大型企业实验平台都有制度约束"——指出了非纯技术性护城河。

4. **experimental_physics_instrumentation_measurement 的 whyResilient**："仪器搭建、校准、噪声排查、样品制备、实验安全和物理解释需要现场经验"——物理约束的描述具体且可验证。

5. **理论/计算物理的 timeWindowNotes** 四个窗口判断均合理，尤其是 gaokao_2030："单靠物理兴趣到 2030 年就业不确定性高"——这个提醒对高中生家长有价值。

6. **biostatistics_pharma_statistics 整体判断**：评级 medium、临床试验约束、合规路径的描述均较为准确，是三族中相对最成熟的子方向条目之一。

7. **所有子方向的 betterSignals** 设计质量较高，普遍给出了可验证的信号而非空洞建议，这是数据库的重要亮点。

---

## 六、最终建议

**不可作为网页第一版样板直接发布**，但经过以下修改后可以：

| 阻塞项 | 建议操作 |
|---|---|
| 量化/精算混装 | 拆分，分别评级 |
| 光电/半导体/量子/材料打包过粗 | 至少拆成两组，量子/前沿材料降级 |
| 公职/事业单位出口缺失 | 新增子方向或显著补充 |
| 跨族 data_analysis_bi 同名 | 重命名或加区分说明 |
| entryRoles 中"算法转岗"不规范 | 修正措辞 |
| 教育方向缺政策风险 | whyRisky 补入 |

完成上述修改后，这 12 个子方向可以作为数学/统计/物理三族同屏的第一版样板发布，同时应在前言或 meta 中显著标注"量子/精算方向待进一步细分"的已知局限。
