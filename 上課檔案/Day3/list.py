'''
l = [1,2,3]
for i in range(len(l)):#0~2
    l[i] = l[i]+1
print(l)
l = [10, 2, 43, 27, 1, 1, 1]
print(max(l))
print(min(l))
l.append(5)
print(l)
l.pop(1)
print(l)
l.insert(3,21)
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)
print(l.count(1))
print(l.index(1))
l.sort()
#[start:end:interval]
del l[0:5:2]
print(l)
'''

# l = [
#     ['O','',''], #0
#     ['','X',''], #1
#     ['','','O'] #2
#     #0  #1  #2
# ]
# print(l[1][1])

# [1, 2, 3, 4, 5]
#  0  1  2  3  4