N, M = input().split() #int(['N','M'])
N, M = int(N), int(M)
l = []
for i in range(N):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    l.append(max(row))
s = sum(l)
print(s)
for i in l:
    if s % i != 0:
        l.remove(i)
if l:
    for i in l:
        print(i, end=' ')
else:
    print(-1)