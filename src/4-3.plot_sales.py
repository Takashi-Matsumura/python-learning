# 4-3.plot_sales.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv")
grouped = df.groupby("商品")["金額"].sum()

grouped.plot(kind="bar", title="商品別売上合計")
plt.ylabel("金額（円）")
plt.tight_layout()
plt.savefig("output/sales_bar_chart.png")
print("棒グラフを output/sales_bar_chart.png に保存しました。")
