from sys import stdin
for year in stdin:
    year = int(year)
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print('閏年')
    else:
        print('平年')