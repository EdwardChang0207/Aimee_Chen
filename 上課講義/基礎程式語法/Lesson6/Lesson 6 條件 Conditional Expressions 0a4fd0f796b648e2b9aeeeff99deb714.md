# Lesson 6 條件 Conditional Expressions

Status: Done
課程進度: L6

# ❓Section I. 什麼是條件

條件是用來判斷一個狀況是否成立，其結果為布林值（True、False）。從L4、L5的運算子單元中，我們知道只有邏輯運算的結果會為布林值。因此我們在設計條件時可以多使用邏輯運算子來進行判斷。

```python
if (condition): #if the condition returns True
else: #if the condition returns False
```

# 🛠Section II. 使用條件

## 一、基本條件使用

使用條件時，最基本的形式為使用單一一個if關鍵字搭配條件內容和條件達成時需要執行的程式。

## Ex.15 建立一個程式判斷使用者的輸入是否為1，若為1，輸出1

```python
user_input = int(input())
if user_input == 1: print(1)
```

[Ex15.py](Lesson%206%20%E6%A2%9D%E4%BB%B6%20Conditional%20Expressions%200a4fd0f796b648e2b9aeeeff99deb714/Ex15.py)

除了可以指定條件達成時的工作內容，也可以指定條件未達成時的工作內容，只要在與if同層加上else即可。

## Ex.16 延續上題，若使用者輸入不為1，則輸出不是1

```python
user_input = int(input())
if user_input == 1: print(1)
else: print('不是1')
```

[Ex16.py](Lesson%206%20%E6%A2%9D%E4%BB%B6%20Conditional%20Expressions%200a4fd0f796b648e2b9aeeeff99deb714/Ex16.py)

## 二、多個條件的判斷

若想要進行多個條件的判斷可以使用elif於if和else之間，其數量沒有上限。

## Ex.17延續上題，若輸入為2時，輸出2。不為1也不為2時，輸出都不是

```python
user_input = int(input())
if user_input == 1: print(1)
elif user_input == 2: print(2)
else: print('都不是')
```

[Ex17.py](Lesson%206%20%E6%A2%9D%E4%BB%B6%20Conditional%20Expressions%200a4fd0f796b648e2b9aeeeff99deb714/Ex17.py)

# 💯重點複習

### 條件必須為布林值，判斷該狀態成立或不成立

### 條件的基本結構為：if…elif…else…

# 🏋️課後練習

## Q6: 判斷以下兩段程式有何不同

```python
if x == 1: print(1)
elif x % 1 == 0: print(x)
```

```python
if x == 1: print(1)
if x % 1 == 0: print(x)
```

# ✏️習題練習

- [ZeroJudge a003](https://zerojudge.tw/ShowProblem?problemid=a003)