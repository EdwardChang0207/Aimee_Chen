n = int(input())
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
r = 0
for i in range(len(l)):
    if l[i] == 0:
        if i == 0:
            r += l[i+1]
        elif i == len(l)-1:
            r += l[i-1]
        else:
            r += min(l[i-1], l[i+1])
