#迴圈 loop
# print(1)
# print(2)
# print(3)

#while loop
# i = 1 #索引值 index
# while i <= 3:
#     print(i)
#     i += 1

#for loop

#range(start(init:0), end, interval(init:1)):number
# from start to end-1, increase interval for each time
# print('case1')
# for i in range(5): #end
#     print(i)

# print('case2')
# for i in range(1, 5): #start, end
#     print(i)

# print('case3')
# for i in range(1, 5, 2):
#     print(i)

# print('decreasing')
# #count from 10 to 1
# for i in range(10, 0, -1):
#     print(i)

#list
# l = ['鮭魚','鮪魚','玉子燒']
# for i in l:
#     print(i)

#string
# s = '鮭魚鮪魚玉子燒'
# for i in s:
#     print(i) #end = '\n'

#continue(skip), break(stop)
for i in range(10): #0~9
    if i % 3 == 0: #是三的倍數->跳過
        continue
    if i == 7:
        break
    print(i)