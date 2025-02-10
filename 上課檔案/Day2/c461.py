a, b, c = input().split() #'0 0 0' -> ['0','0','0'] -> a = '0', b = '0', c = '0'
a, b, c = int(a), int(b), int(c)
r = False
if (a and b) == c:
    print('AND')
    r = True
if (a or b) == c:
    print('OR')
    r = True
if ((a or b) and (not(a and b))) == c:
    print('XOR')
    r = True
if (not r):
    print('IMPOSSIBLE')
