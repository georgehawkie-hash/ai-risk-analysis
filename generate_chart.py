"""
风险全景图生成脚本

数据：本工具子方向风险评级（11 大类 × 100+ 子方向）
排序：综合得分 = 高风险% + 中高风险% × 0.6（仅用于呈现顺序，不构成定量预测）
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 字体配置
matplotlib.rcParams['font.sans-serif'] = [
    'Microsoft YaHei', 'PingFang SC', 'SimHei',
    'Noto Sans CJK SC', 'Source Han Sans SC',
]
matplotlib.rcParams['axes.unicode_minus'] = False

# 11 个理工大类（已将英文缩写改为中文：IC → 集成电路，BME → 生物医学工程）
majors = [
    '计算机 / 软件 / 数据 / AI',
    '数学 / 统计 / 物理',
    '电子 / 微电子 / 集成电路',
    '电气 / 能源动力',
    '自动化 / 机器人 / 智能制造',
    '机械 / 仪器 / 智能制造工程',
    '土木 / 建筑 / 水利 / 测绘 / 交通 / 环境',
    '材料 / 化学 / 化工 / 制药',
    '生物 / 生物工程 / 生物医学工程',
    '工业工程 / 管理科学 / 物流',
    '交叉学科 / 新工科',
]

# 5 级风险分布（来自 HTML 主矩阵中各大类的子方向 aria-label 计数）
data = {
    'high':        [2, 1, 0, 3, 4, 2, 7, 5, 4, 7, 7],
    'medium_high': [7, 6, 0, 6, 5, 5, 6, 7, 14, 7, 8],
    'medium':      [1, 7, 3, 5, 7, 8, 5, 10, 3, 6, 2],
    'low':         [0, 0, 4, 5, 3, 4, 4, 0, 1, 2, 2],
    'opportunity': [1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 7],
}

# 百分比 + 综合得分
totals = [sum(data[k][i] for k in data) for i in range(len(majors))]
pct = {k: [data[k][i] / totals[i] * 100 for i in range(len(majors))] for k in data}
risk_score = [pct['high'][i] + pct['medium_high'][i] * 0.6 for i in range(len(majors))]

# 按综合得分降序排序（风险高的在上）
order = np.argsort(risk_score)[::-1]
majors_sorted = [majors[i] for i in order]
pct_sorted = {k: [pct[k][i] for i in order] for k in pct}
totals_sorted = [totals[i] for i in order]
scores_sorted = [risk_score[i] for i in order]

# 颜色配置（与最新 HTML 主题一致：更深、更耐看）
colors = {
    'high':        '#c0392b',   # red
    'medium_high': '#e67e22',   # orange
    'medium':      '#d4a017',   # yellow
    'low':         '#2e7d32',   # green
    'opportunity': '#1c4e80',   # blue
}
labels = {
    'high':        '高风险',
    'medium_high': '中高风险',
    'medium':      '中等分化',
    'low':         '低风险',
    'opportunity': '机会',
}
# 段内 % 标注颜色（黄色背景需深字）
text_colors = {
    'high':        '#fff',
    'medium_high': '#fff',
    'medium':      '#3d2f00',
    'low':         '#fff',
    'opportunity': '#fff',
}

# 画布
fig, ax = plt.subplots(figsize=(15, 8.4))
fig.patch.set_facecolor('#fafaf8')
ax.set_facecolor('#fafaf8')

y = np.arange(len(majors_sorted))
bar_height = 0.62
left = np.zeros(len(majors_sorted))

# 堆叠水平条
for key in ['high', 'medium_high', 'medium', 'low', 'opportunity']:
    vals = pct_sorted[key]
    bars = ax.barh(
        y, vals, bar_height, left=left, color=colors[key],
        label=labels[key], edgecolor='white', linewidth=0.8,
    )
    for j, v in enumerate(vals):
        if v >= 8:
            cx = left[j] + v / 2
            ax.text(
                cx, y[j], f'{v:.0f}%',
                ha='center', va='center',
                fontsize=10.5, fontweight='bold',
                color=text_colors[key],
            )
    left += vals

# 右侧标注：子方向数 + 综合得分
for j in range(len(majors_sorted)):
    ax.text(
        103, y[j], f'{totals_sorted[j]} 个',
        ha='left', va='center',
        fontsize=10.5, color='#6a6f76',
    )
    ax.text(
        122, y[j], f'{scores_sorted[j]:.0f}',
        ha='center', va='center',
        fontsize=11.5, color='#1c4e80', fontweight='bold',
    )

# Y 轴：专业名称
ax.set_yticks(y)
ax.set_yticklabels(majors_sorted, fontsize=13, fontweight='bold', color='#1a1a1a')
ax.set_xlim(0, 132)
ax.invert_yaxis()

# 移除全部坐标轴装饰
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
ax.tick_params(axis='y', which='both', left=False)

# 标题 + 副标题
fig.suptitle('')  # 清空默认
fig.text(
    0.07, 0.955,
    '11 大类理工专业 · 入门岗位 AI 风险分布',
    fontsize=22, fontweight='bold', color='#1a1a1a', ha='left',
)
fig.text(
    0.07, 0.918,
    '每行 = 一个专业大类内全部子方向按风险等级的占比 · 排序依据：综合得分 = 高风险% + 中高风险% × 0.6',
    fontsize=12, color='#6a6f76', ha='left',
)

# 轴方向提示（左红右绿）
fig.text(
    0.275, 0.876, '← 入门压力大',
    fontsize=11.5, fontweight='bold', color='#c0392b', ha='left',
)
fig.text(
    0.66, 0.876, '入门压力小 →',
    fontsize=11.5, fontweight='bold', color='#2e7d32', ha='right',
)

# 右侧列头
fig.text(
    0.86, 0.876, '子方向数',
    fontsize=10.5, fontweight='bold', color='#6a6f76', ha='center',
)
fig.text(
    0.937, 0.876, '综合得分',
    fontsize=10.5, fontweight='bold', color='#1c4e80', ha='center',
)

# 图例（底部居中）
legend = ax.legend(
    loc='upper center', bbox_to_anchor=(0.5, -0.04),
    ncol=5, frameon=False, fontsize=12.5,
    handlelength=1.4, handleheight=1.0,
    columnspacing=2.0,
)

# 页脚说明
fig.text(
    0.07, 0.018,
    '注：0.6 权重仅用于呈现排序，不构成定量预测  ·  数据基于本工具 11 大类 × 100+ 子方向独立评级',
    fontsize=10, color='#9da3ab', ha='left', style='italic',
)
fig.text(
    0.93, 0.018,
    '© 2026 · 2026 理工科 AI 就业风险矩阵',
    fontsize=10, color='#9da3ab', ha='right', style='italic',
)

# 边距
plt.subplots_adjust(left=0.22, right=0.94, top=0.84, bottom=0.08)

plt.savefig(
    r'C:\Users\msn_w\Desktop\Workspace\output\ai-risk-analysis\risk_overview.png',
    dpi=220, bbox_inches='tight', facecolor='#fafaf8', edgecolor='none',
    pad_inches=0.2,
)
print('Chart saved.')
