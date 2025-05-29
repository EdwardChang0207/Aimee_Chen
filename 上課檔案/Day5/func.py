# def plus(a,b):
#     print(a+b)
    # return a+b

# c = plus(2,3) #-> 5
# print(c)

# def remove_from_list(A:list)->list:
#     A.pop(0)
#     return A

# print(remove_from_list([1,2,3]))

# l = [1,2,3]
# l.pop()

# def plus(a,b):
#     return a+b
# def minus(a,b):
#     return a-b
# def mult(a,b):
#     return a*b
# def divde(a,b):
#     return a/b

# print(mult(plus(2,3)-mult(2,8), divde(9,3)))

# import random as r 
# from random import randint
# ans = randint(1,100)
# upper, lower = 100, 1
# guess = -1
# while guess != ans:
#     print(f'{lower}~{upper}')
#     guess = int(input())
#     if guess > ans:
#         upper = guess
#     elif guess < ans:
#         lower = guess
# print('correct')

# import time
# print('123')
# time.sleep(8)
# print('456')

import toolbox
print(toolbox.plus(2,3))