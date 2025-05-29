import openpyxl
def file_init():
    wb = openpyxl.Workbook()
    wb.save('上課檔案/Day9/result.xlsx')