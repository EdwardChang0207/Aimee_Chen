# x = [0,1,2,3,4,5]
# xy = [
#     [0, 1, 2],#A
#     [3, 4, 5],#B
#     [6, 7, 8] #C
# ]
#xy = [A,B,C]
#      0 1 2
#xy[1] -> [3,4,5]
#xy[1][1]

A = [
    [0, 1, 2],#A 0
    [3, 4, 5],#B 1
    [6, 7, 8], #C 2
    [9, 10, 11] #D 3
    #0  1   2
]
print(A[0])
# A[1] -> B
#A[1][1]
# A[0][0] -> A[1][0] -> A[2][0] 
# A[0][1] -> A[1][1] -> A[2][1]
# A[0][2] -> A[1][2] -> A[2][2]
# A[0][3] -> A[1][3] -> A[2][3]

#A:4x3
#A = [A,B,C,D] -> A' = [D,C,B,A]
# A.reverse()
# print(*A, sep='\n') * -> for all
# At = [
#     [0, 3, 6, 9],
#     [1, 4, 7, 10],
#     [2, 5, 8, 11]
# ]
#At:3x4
# At = []
# for col in range(len(A[0])): #換col
#     r = []
#     for row in range(len(A)): #換row
#         r.append(A[row][col])
#     At.append(r)
        
# print(*At, sep='\n')