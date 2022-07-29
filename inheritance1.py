
import openpyxl

book = openpyxl.load_workbook("C:\\Users\\KARTHIK\\Desktop\\pythondata.xlsx")

sheet = book.active

cell = sheet.cell(row=3, column=4)
print(cell.value)