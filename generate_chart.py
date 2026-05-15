import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'PingFang SC', 'Noto Sans CJK SC']
matplotlib.rcParams['axes.unicode_minus'] = False

majors = [
    '计算机/软件/数据/AI',
    '数学/统计/物理',
    '电子/微电子/IC',
    '电气/能源动力',
    '自动化/机器人/智能制造',
    '机械/仪器/智能制造工程',
    '土木/建筑/水利/测绘/交通/环境',
    '材料/化学/化工/制药',
    '生物/生物工程/BME',
    '工业工程/管科/物流',
    '交叉学科/新工科',
]

data = {
    'high':        [2, 1, 0, 3, 4, 2, 7, 5, 4, 7, 7],
    'medium_high': [7, 6, 0, 6, 5, 5, 6, 7,14, 7, 8],
    'medium':      [1, 7, 3, 5, 7, 8, 5,10, 3, 6, 2],
    'low':         [0, 0, 4, 5, 3, 4, 4, 0, 1, 2, 2],
    'opportunity': [1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 7],
}

totals = [sum(data[k][i] for k in data) for i in range(len(majors))]
pct = {k: [data[k][i] / totals[i] * 100 for i in range(len(majors))] for k in data}

risk_score = [pct['high'][i] + pct['medium_high'][i] * 0.6 for i in range(len(majors))]
order = np.argsort(risk_score)[::-1]

majors_sorted = [majors[i] for i in order]
pct_sorted = {k: [pct[k][i] for i in order] for k in pct}
totals_sorted = [totals[i] for i in order]

colors = {
    'high':        '#d95f5f',
    'medium_high': '#f2a65a',
    'medium':      '#f2d16b',
    'low':         '#67b26f',
    'opportunity': '#4c78a8',
}
labels = {
    'high':        '高风险',
    'medium_high': '中高风险',
    'medium':      '中等分化',
    'low':         '低风险',
    'opportunity': '机会',
}

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#faf9f5')
ax.set_facecolor('#faf9f5')

y = np.arange(len(majors_sorted))
bar_height = 0.55
left = np.zeros(len(majors_sorted))

for key in ['high', 'medium_high', 'medium', 'low', 'opportunity']:
    vals = pct_sorted[key]
    bars = ax.barh(y, vals, bar_height, left=left, color=colors[key], label=labels[key], edgecolor='white', linewidth=0.5)
    for j, (bar, v) in enumerate(zip(bars, vals)):
        if v >= 8:
            cx = left[j] + v / 2
            ax.text(cx, y[j], f'{v:.0f}%', ha='center', va='center', fontsize=9, fontweight='bold',
                    color='#fff' if key in ('high', 'opportunity') else '#333')
    left += vals

for j in range(len(majors_sorted)):
    ax.text(101, y[j], f'({totals_sorted[j]})', ha='left', va='center', fontsize=9, color='#999')

ax.set_yticks(y)
ax.set_yticklabels(majors_sorted, fontsize=12, fontweight='bold')
ax.set_xlim(0, 112)
ax.set_xlabel('')
ax.invert_yaxis()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
ax.tick_params(axis='y', which='both', left=False)

legend = ax.legend(
    loc='upper center', bbox_to_anchor=(0.45, 1.08),
    ncol=5, frameon=False, fontsize=11, handlelength=1.2, handleheight=0.9,
    columnspacing=1.5
)

ax.set_title('各专业子方向风险分布', fontsize=18, fontweight='bold', pad=40, color='#202124')

plt.tight_layout()
plt.savefig(
    r'C:\Users\msn_w\Desktop\Workspace\output\ai-risk-analysis\risk_overview.png',
    dpi=200, bbox_inches='tight', facecolor='#faf9f5', edgecolor='none'
)
print('Chart saved.')
