import os
import shutil
import glob
def move_file(path):
    pattern = f'{path}/*.xlsx'
    matching_files = glob.glob(pattern)
    for f in matching_files:
        filename = f.split('/')[-1]
        #['上課檔案','Day16','BOM_file','300-00008-r4-effective-BOM (2).xlsx']
        os.rename(f, f"上課檔案/Day16/BOM_file/{filename}")
    