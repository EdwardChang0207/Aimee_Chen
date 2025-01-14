# Lesson 7 迴圈 Loop

Status: Done
課程進度: L7

# ❓Section I. 什麼是迴圈

迴圈(loop)就是重複的概念，可以幫助我們省略反覆的動作，迴圈主要分為for迴圈(for loop)和while迴圈(while loop)，兩者皆可完成一樣的功能，唯獨適合的情境不同，所以使用哪個迴圈並不會影響程式結果。

```python
#未使用迴圈
print(1)
print(1)
print(1)
print(1)
print(1)

#使用迴圈
for i in range(5):
	print(1)
```

# 🔢Section II. For迴圈 For-Loop

for迴圈(For Loop)又可以稱為"計次的迴圈”，用於"已知次數”的迴圈。for迴圈內會有一個index(索引值)，這個index我們通常使用"i”來表示，依據迴圈的範圍，index會暫存目前正執行的值。

```python
for (index) in (range):
	process
```

## 一、範圍-Range

### 1.範圍函式-Range function

range()可以產生一個遞增或是遞減的數列，其值為start~end-1，每次增加或減少interval。若只在括號內輸入一個數，該數會視為end，start預設值為0，interval預設值為1。

**range function:**

```python
range(start, end, interval)
```

## Ex.18 使用for loop輸出1~100

```python
for i in range(1, 101):
	print(i, end=' ')
```

[ex18.py](Lesson%207%20%E8%BF%B4%E5%9C%88%20Loop%2089bbd8f6d4654a1caa7e8d06a3892b55/ex18.py)

### 2.串列-List

使用串列(List)當作for迴圈範圍時，其中的index會將串列中的各項元素(Element)分別取出，我們便可以使用index去讀取其中的值(Value)，但其存取形式為參照(Reference)，若我們改變index的數值，不會對原串列中的元素做出修改。

```python
list1 = [0, 1, 2, 3, 4]
for i in list1:
	i += 1
	print(i, end=' ')
print(list1)
```

## Ex.19 使用for loop將串列中的數值修改為原數值*2後輸出

```python
list1 = [1, 2, 3, 4, 5]
for i in range(len(list1)):
	list1[i] *= 2
print(list1)
```

[ex19.py](Lesson%207%20%E8%BF%B4%E5%9C%88%20Loop%2089bbd8f6d4654a1caa7e8d06a3892b55/ex19.py)

# 🔂Section III. While迴圈-While Loop

while迴圈(while loop)又稱為"條件迴圈”，我們可以把它想像成不斷執行的if，在條件達成(return True)時，會不斷的執行。常用於"未知次數的迴圈程式。

```python
i = 0
while i < 3:
	print(i)
	i += 1
```

## Ex.20 判斷使用者輸入的帳號密碼是否正確，若正確輸出你已登入，不正確則輸出錯誤並要求繼續輸入

```python
username = 'hello'
password = '123'
login = False
while not login:
	username_input = input()
	password_input = input()
	if username_input == username and password_input == password:
		login = True
		print('已登入')
	else:
		print('錯誤') 
```

[ex20.py](Lesson%207%20%E8%BF%B4%E5%9C%88%20Loop%2089bbd8f6d4654a1caa7e8d06a3892b55/ex20.py)

# ⛔繼續Continue(skip)&停止Break(stop)

在迴圈(Loop)中，使用Continue和Break可以跳過和終止整個迴圈，如下所示。

```python
for i in range(20):
	if i % 4 == 0: #i可以被4整除時，跳過該次迴圈
		continue
	elif i == 10: #i等於10時，終止迴圈
		break
	print(i)
```

# 💯重點複習

### 迴圈(loop)就是重複的概念，可以幫助我們省略反覆的動作

### 迴圈分為for loop與while loop，for loop常用於已知次數的迴圈，while loop則用於未知次數的迴圈

### for loop需要提供一個範圍當作執行的依據，範圍可以使用range()也可以使用一個list

### while loop可以想像成不停重複判斷的if，在條件達成(True)時，就會不停重複

### 使用Continue可以跳過某一次迴圈，使用Break可以停止整個迴圈

# 🏋️課後練習

## Q9: 分別使用for loop和whlie loop撰寫一個程式，使其可以找到使用者輸入數值的因數，並存於一個串列中，再將其輸出

[Q7.py](Lesson%207%20%E8%BF%B4%E5%9C%88%20Loop%2089bbd8f6d4654a1caa7e8d06a3892b55/Q7.py)