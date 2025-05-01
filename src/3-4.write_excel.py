# 3-4.write_excel.py

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "売上データ"

ws.append(["日付", "商品", "金額"])
ws.append(["2025/05/01", "ペン", 120])
ws.append(["2025/05/02", "ノート", 230])

wb.save("output/sales.xlsx")
print("Excelファイルを出力しました。")
