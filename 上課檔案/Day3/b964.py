n = int(input())
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
for i in s:
    print(i, end=' ')
print()

if s[0] >= 60:
    print('best case')
    print(s[0])
elif s[len(s)-1] < 60:
    print(s[len(s)-1])
    print('worst case')
else:
    #[不及格[]|[]及格]
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])
            break
