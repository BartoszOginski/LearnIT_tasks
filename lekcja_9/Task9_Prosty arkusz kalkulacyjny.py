from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Wydatki"

ws.append(["Wydatek", "Wartość"])
ws.append(["Jedzenie", 500])
ws.append(["Prad", 238])
ws.append(["Internet", 78])
ws.append(["Suma:","=SUM(B2:B4)"])

wb.save("finanse.xlsx")