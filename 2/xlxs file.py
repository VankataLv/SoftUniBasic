from openpyxl import Workbook

workbook = Workbook()
current_sheet = workbook.active

current_sheet["A1"] = "1"
current_sheet["B1"] = "1"
current_sheet["C1"] = "1"
current_sheet["A2"] = "1"
current_sheet["B2"] = "1"
current_sheet["C2"] = "1"

workbook.save(filename='example_excel.xlsx')
