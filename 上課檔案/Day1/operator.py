#Numbers
'''
+, -, *, / -easy
a**b -> 指數(次方):a的b次方, 補充：0.5 == 1/2, 所以 a**0.5 == a開根號
a%b -> 取餘數
a//b -> 取商數
'''

print(3**2)
print(9**0.5)
print(30%7)
print(30//7)

#Logic
'''
<, >, >=, <=, ==(equal), !=(not equal)
in(在裡面), is(equal)
'''
print(3 < 2)
print(3 == 2)
print(3 != 2)
print(3 >= 2)
a = [1, 2, 3]
print(5 in a)
print(1 is int)

#Boolean
'''
not(反閘)
不錯喔 -> not False  -> True
錯 -> False
不行 -> not True -> False
行 -> True
or(或、聯集)
數學 -> a 英文 -> b 3000 -> c
(真值表)
a or b -> c
T    F    T
F    T    T
T    T    T
F    F    F
and(且、交集)
報告 -> a , 客戶 -> b boss -> c
a and b -> c
T     T    T
T     F    F
F     T    F
F     F    F
xor(斥或閘)
雞腿 -> a, 排骨 -> b, 奇摩子 -> c
a xor b -> c
T     F    T
F     T    T
F     F    F
T     T    T
'''
# print(not False)
a, b = False, False
# print(a or b)
# print(a and b)
print((a or b) and (not(a and b)))

#String
print('1'+'2')
print('1' * 5)

#List
print([1, 2] + [3, 4])
print([1, 2] * 3)

#str 跟 list 可以做的事幾乎一樣