from del_empty_row import del_empty
from pivot import pivot
from sku_sum import sku_sum
def main():
    file_name = '上課檔案/Day8/Pivot.xlsx'
    del_empty(file_name)
    pivot(file_name)
    sku_sum(file_name)