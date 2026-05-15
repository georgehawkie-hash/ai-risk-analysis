"""
社交卡片图生成脚本

输出 1200×630 的 social_card.png，用于：
- 微信链接分享缩略图
- 微博 / Twitter / Facebook / LinkedIn 等社交平台的 og:image
- 邮件转发的 hero 图
"""
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = [
    'Microsoft YaHei', 'PingFang SC', 'SimHei',
    'Noto Sans CJK SC', 'Source Han Sans SC',
]
matplotlib.rcParams['axes.unicode_minus'] = False

# 1200×630 标准尺寸（Facebook / Twitter / 微信优选比例）
fig, ax = plt.subplots(figsize=(12, 6.3))
fig.patch.set_facecolor('#fafaf8')
ax.set_facecolor('#fafaf8')

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# 顶部 kicker（红色装饰条 + 标签）
ax.plot([4, 9.5], [91, 91], color='#c0392b', linewidth=5, solid_capstyle='butt')
ax.text(11.5, 91, '任务级 AI 暴露分析  ·  2026 - 05',
        fontsize=12.5, color='#6a6f76', fontweight='bold', va='center')

# 右上：5 级风险编码彩点
risk_colors = ['#c0392b', '#e67e22', '#d4a017', '#2e7d32', '#1c4e80']
risk_labels = ['高', '中高', '中', '低', '机会']
for i, c in enumerate(risk_colors):
    cx = 81 + i * 3.2
    circle = plt.Circle((cx, 91), 1.0, color=c, zorder=5)
    ax.add_patch(circle)
ax.text(95.5, 91, '5 级风险编码',
        fontsize=10, color='#6a6f76', va='center', style='italic')

# 主标题（两行）
ax.text(4, 73, '2026 理工科 AI',
        fontsize=46, fontweight='bold', color='#1a1a1a', va='center')
ax.text(4, 60, '就业风险矩阵',
        fontsize=46, fontweight='bold', color='#1a1a1a', va='center')

# 副标题
ax.text(4, 49, 'VOLUME 2026  ·  高考家长 · 大学生 · 研究生',
        fontsize=11.5, fontweight='bold', color='#1c4e80', va='center')

# 左竖线 + thesis
ax.plot([4, 4], [33, 42], color='#c0392b', linewidth=3, solid_capstyle='butt')
ax.text(6, 39, 'AI 不按专业名淘汰人，它在重排"入行路径"',
        fontsize=18, fontweight='bold', color='#1a1a1a', va='center')
ax.text(6, 33, '只做标准任务的人先被压缩，能承担系统和责任的人更有位置',
        fontsize=12.5, color='#2d2d30', va='center')

# 数据 spec 横条（顶 / 底分隔线）
ax.plot([4, 96], [23.5, 23.5], color='#1a1a1a', linewidth=1.5, solid_capstyle='butt')
ax.plot([4, 96], [6.5, 6.5], color='#e5e7eb', linewidth=1, solid_capstyle='butt')

# 5 个数字
stats = [
    ('11', '专业大类'),
    ('100+', '子方向'),
    ('4', '毕业窗口'),
    ('24', '公开数据源'),
    ('16/16', '已核对'),
]
n = len(stats)
left_x, right_x = 4, 96
gap = (right_x - left_x) / n
for i, (value, label) in enumerate(stats):
    cx = left_x + gap * (i + 0.5)
    ax.text(cx, 16.5, value, fontsize=27, fontweight='bold',
            color='#1a1a1a', ha='center', va='center')
    ax.text(cx, 10, label, fontsize=11, color='#6a6f76',
            fontweight='bold', ha='center', va='center')
    # 分隔细线
    if i > 0:
        ax.plot([left_x + gap * i, left_x + gap * i], [9, 22],
                color='#e5e7eb', linewidth=1, solid_capstyle='butt')

# 底部 URL
ax.text(50, 2.5, 'georgehawkie-hash.github.io/ai-risk-analysis',
        fontsize=10.5, color='#9da3ab', ha='center', va='center', style='italic')

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

plt.savefig(
    r'C:\Users\msn_w\Desktop\Workspace\output\ai-risk-analysis\social_card.png',
    dpi=100,                          # 12×6.3 in @ 100 DPI = 1200×630 px
    facecolor='#fafaf8',
    edgecolor='none',
    pad_inches=0,
    bbox_inches=None,
)
print('Social card saved: 1200×630 px')
