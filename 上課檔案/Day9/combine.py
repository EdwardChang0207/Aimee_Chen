import openpyxl
import os
import load_init_file
import file_init
import title_init
file_init.file_init()
source_folder = '上課檔案/Day9/source'
file_list = os.listdir(source_folder)
title_init.title_init(source_folder+'/'+file_list[0])
for path in file_list:
    load_init_file.load_init_file(source_folder+'/'+path)

