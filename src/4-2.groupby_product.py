# 4-2.groupby_product.py

import pandas as pd

df = pd.read_csv("data/sales.csv")
grouped = df.groupby("商品")["金額"].sum()

print("商品別 売上合計:")
print(grouped)
