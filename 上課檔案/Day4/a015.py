#row, col -> size of m
row, col = input().split()
row, col = int(row), int(col)
m = [] #m:r*c
for i in range(row): #建立m
    r = input().split()#r:m的一個row
    for i in range(len(r)): #轉整數
        r[i] = int(r[i])
    m.append(r)#把一個row新增到ｍ

mt = []#mt:轉置矩陣
#col
for c in range(col): #換col
    #row
    t = []#t:mt的一個row
    for r in range(row): #換row
        t.append(m[r][c])
    mt.append(t)

for r in mt: #loop mt的每一個row
    print(*r) #輸出mt的row中所有的元素