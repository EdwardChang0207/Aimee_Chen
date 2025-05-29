a, b = input().split()
a, b = int(a), int(b)
n = int(input())
r = 0
for i in range(n):
    l = input().split()
    for j in range(len(l)):
        l[j] = int(l[j])
    l.sort()
    for i in range(len(l)): #[負|正]
        if l[i] >= 0:
            l = l[i:len(l)]
            break
        if l[i] < 0:
            print(l[i])
            l.remove(-1*l[i])
    if (a in l) and (b in l):
        r += 1
print(r)