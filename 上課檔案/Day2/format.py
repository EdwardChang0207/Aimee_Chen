# print('班級','姓名','座號')
# print('101','王大明','1 ')
# print('101','張明 ','11')

# %
# print('%3s %5s %2s' % ('cls','name','no')) #標題
# cls = 101
# name = 'alan'
# no = 1
# print('%3s %5s %2s' % (cls, name, no)) #alan
# cls = 101
# name = 'kevin'
# no = 11
# print('%3s %5s %2s' % (cls, name, no)) #kevin

print('your number is %5s, you are %sth customer today' % (1000, 10))# -> print('your number is', str(10))
print('your number is %5d' % (1000))# -> print('your number is', str(int(10)))
print('your number is %5.2f' % (1000))# -> print('your number is', str(float(10)))

#格式符號
'''
%{a}s -> str
%{a}d -> int
%{a}.{b}f -> float
{a}:至少輸出 a個字元，如果不夠就在前面補空格，如果超過就不管
{b}:輸出到小數點後 b位數
'''

#format()
print('your number is {1:2,d}, you are {0:2d}th customer today'.format(100000000, 10))

#f-string f:function
number = 100000000
no = 10
print(f'your number is {number:,.2f}, you are {no}th customer today')
