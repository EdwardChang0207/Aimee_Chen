a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
D = b**2 - 4*(a*c)
if D > 0:
    x1, x2 = int((-1 * b + D**0.5)/(2 * a)), int((-1 * b - D**0.5)/(2 * a))
    print('Two different roots x1=%d , x2=%d' % (x1,x2))
elif D == 0:
    x = int((-1 * b + D**0.5)/(2 * a))
    print('Two same roots x={}'.format(x))
else:
    print('No real root')