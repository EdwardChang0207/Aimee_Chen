import openpyxl
def source_init(path):
    source_file = openpyxl.load_workbook(path)
    sheet = source_file.worksheets[1]
    sheet.delete_cols(1,4)
    sheet.delete_cols(2,1)
    sheet.delete_cols(3,1)
    sheet.delete_cols(5,9)
    sheet.delete_rows(1,3)
    source_file.save('上課檔案/Day10/price.xlsx')