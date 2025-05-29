def rotate(B):
    #轉置
    BT = []
    for col in range(len(B[0])):
        r = []
        for row in range(len(B)):
            r.append(B[row][col])
        BT.append(r)
    B = BT
    #flip
    B.reverse()
    return B

def filp(B):
    B.reverse()
    return B

R, C, M = input().split()
R, C, M = int(R), int(C), int(M) #

B = []
for row in range(R):
    r = input().split()
    for i in range(len(r)):
        r[i] = int(r[i])
    B.append(r)

k = input().split() # A -> B
k.reverse()# B -> A

for i in k:
    if i == '0':#rotation
        B = rotate(B)
    else: #flip
        B = filp(B)

print(len(B), len(B[0]))
for row in B:
    print(*row)