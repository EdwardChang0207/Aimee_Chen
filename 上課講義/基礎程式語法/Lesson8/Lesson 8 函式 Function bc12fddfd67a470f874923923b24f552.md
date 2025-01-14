# Lesson 8 函式 Function

Status: Done
課程進度: L8

<aside>
💡 編、著:張雲翔，未經許可禁止公開散布、營利使用

</aside>

<aside>
💡 本課重點:認識函式、建立函式、使用模組

</aside>

# 🧑‍🔧函式(Functions)

函式(Function)可以想像成一個機器，可以分為三個部分討論:輸入(Input)、功能(Process)、輸出(Output)，就像L1討論程式架構一樣，在程式內使用函式(Function)也可以想成在一個大程式中使用很多個小程式來達到指定的功能，使用函式也可以讓專案更容易測試和管理。

```python
def funciton_name(p1, p2, p3...): #parameters are the inputs u provide
	write ur programs here... #process
	return output #output
```

## 🤜內建(built in)函式

內建的函式即是python原本就已經建立的函式，例如:print()、intput()…
我們可以直接使用函式的名稱呼叫函式使用

```python
print('hello')
x = input()
```

| function_name | function |
| --- | --- |
| abs(value) | 取絕對值 |
| max(v1, v2, v3) | 取最大值(可直接放入串列) |
| min(v1, v2, v3) | 取最小值(可直接放入串列) |
| pow(a, b) | a的b次方 |
| round(a) | 尋找最接近a的整數 |
| sum(list) | 計算總和，輸入為串列 |
| type(a) | a的資料型態 |

## ⚙️自訂函式

自訂函式就是自行創造一個函式並做使用，若要創建一個函式，需要使用關鍵字"def”，1並指定參數(parameter)和輸出(return)

```python
def plus(p1, p2):
	ans = p1 + p2
	return ans

print(plus(1,4))
```

## 🐦外部函式

外部函式就是從外部的函式庫引入函式進行使用，引入的函式庫又可以稱為模組(modules)，引入模組(modules)時，需要使用關鍵字"import”，如果要使用模組內的函式，需要使用以下方法:modules_name.function_name()

```python
import random as r
a = r.randint(10)
print(a)
```

| module_name | discription |
| --- | --- |
| sys | 與系統互動相關功能(built in) |
| math | 各種數學函式(built in) |
| random | 產生隨機數(built in) |
| time | 時間相關函式(built in) |
| numpy | 資料處理相關函式(third party) |

## Ex.1使用函式製作一個包含加減乘除功能的計算機

### 解題思路:

已知需要加減乘除4種功能，建立4個function

### 參考解答:

```python
def plus(a, b):
	return(a+b)

def minus(a,b):
	return(a-b)

def mutiple(a,b):
	return(a*b)

def devide(a,b):
	return(a/b)

user_input = input()
user_input = user_input.split()
if user_input[1] == '+':
	plus(int(user_input[0]), int(user_input[2]))
elif user_input[1] == '-':
	minus(int(user_input[0]), int(user_input[2]))
elif user_input[1] == '*':
	mutiple(int(user_input[0]), int(user_input[2]))
elif user_input[1] == '/':
	devide(int(user_input[0]), int(user_input[2]))
```