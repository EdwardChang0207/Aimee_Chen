import glob
import openpyxl
def combine_BOM(path):
    #create new wk, ws
    ME_BOM_ALL = openpyxl.Workbook()
    ME_BOM_ALL_SW = ME_BOM_ALL.worksheets[0]
    
    #search all xlsx files
    pattern = f'{path}/*.xlsx'
    matching_files = glob.glob(pattern)

    #判斷title是否已經存入
    title = False

    #對每一個檔案進行處理
    for f in matching_files:
        #抓取filename
        file_name = f.split('/')[-1]
        file_name = file_name.split('-')[0:3]
        file_name[2] = file_name[2][1::]
        #判斷revision是否要補0
        if len(file_name[2]) == 1: file_name[2] = '0'+ file_name[2]
        #合併BOM_NO
        BOM_NO = f'{file_name[0]}-{file_name[1]}-{file_name[2]}'
        #載入來源檔
        wk = openpyxl.load_workbook(f)
        ws = wk.worksheets[0]

        titles = []#存取row1的標題
        for col in range(1, ws.max_column+1):
            titles.append(ws.cell(row=1, column=col).value)
        #判斷vendor是否存在 if yes -> del
        if 'Vendor 1' in titles:
            start = titles.index('Vendor 1')
            end = titles.index('Manufacturer 1')
            count = end-start
            ws.delete_cols(start+1, count)
        #判斷 sub rank是否存在 if -> del 0, col
        if 'Sub. rank' in titles:
            rm_row = []
            for r in range(1, ws.max_row+1):
                if ws.cell(row=r, column=2).value == 0:
                    rm_row.append(r)
            rm_row.reverse()
            for r in rm_row:
                ws.delete_rows(r,1)
            ws.delete_cols(2,1)

        #記錄輸出檔案目前寫入到哪一個row
        target_file_write_start_point = ME_BOM_ALL_SW.max_row

        #寫入A,B col的標題
        if not title: 
            t = 1 #是第一個檔案 -> 從row 1開始寫入
            ME_BOM_ALL_SW.cell(row=1, column=1).value = 'BOM_version'
            ME_BOM_ALL_SW.cell(row=1, column=2).value = 'pn_version'

        else: t = 2 #不是第一個檔案 -> 從row 2開始寫入

        #讀取來源檔案的每一個cell
        for r in range(t, ws.max_row+1): #loop through every row
            if ws.cell(row=r,column=1).value == 'Total': break #if 到了total那一個row -> stop

            if r > 1:#不是標題的row
                #寫入BOM_NO
                ME_BOM_ALL_SW.cell(row=target_file_write_start_point+r-1, column=1).value = BOM_NO
                #寫入PN
                item_number = ws.cell(row=r, column=2).value
                revision = str(ws.cell(row=r, column=3).value)
                #revision < 10 -> 補0
                if len(revision) == 1: revision = '0'+revision
                ME_BOM_ALL_SW.cell(row=target_file_write_start_point+r-1, column=2).value = f'{item_number}-{revision}'
            
            for c in range(1, ws.max_column+1):#loop through every col
                i = ws.cell(row=r, column=c).value
                target_cell = ME_BOM_ALL_SW.cell(row=target_file_write_start_point+r-1, column=c+2)
                target_cell.value = i
        ME_BOM_ALL.save('上課檔案/Day16/result.xlsx')
        title = True


