# Lesson 4 運算子 Operator

Status: Done
課程進度: L4

<aside>
💡 改動請註解於comment

</aside>

<aside>
💡 學習指標:數值運算、邏輯運算

</aside>

# ❓什麼是運算子 Operator

運算子可以用數學運算符號來想像，他可以代表某一種運算方法，但在程式中的運算子不限於數學方法，也有邏輯運算等運算子。

## Ex.9 輸入兩個數字a, b，輸出兩數相加、相減、相乘、相除後的結果

```python
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
```

[Ex9.py](Lesson%204%20%E9%81%8B%E7%AE%97%E5%AD%90%20Operator%20e3d81e9586904e1a9ed2f3df2719dcf0/Ex9.py)

# ➕運算子應用

## 一、數學運算子

數學運算子可以幫我們做常見的數學運算，加減乘除等，計算結果為數值。

| **運算子** | **功能** |
| --- | --- |
| a + b | 相加 |
| a - b | 相減 |
| a * b | 相乘 |
| a / b | 相除 |
| a ** b | a的b次方 |
| a // b | a除以b後取商 |
| a % b | a除以b後取餘數 |

### (1)指數與底數: a的b次方

在數學中，常會看到平方、立方等寫法，例如2的3次方會寫成2³，其中2為底數，3為指數。

$$
2^2 = 4 \\
4^\dfrac{1}{2} = √4 = 2
$$

### (2)商數與餘數: 分組問題

在除法中，常會處理分組分堆的問題，其中組別上限就是商，剩下來尚未分到組的就是餘。

## Ex.10 製作一計算機，計算a的b次方

```python
a = int(input())
b = int(input())
print(a**b)
```

[Ex10.py](Lesson%204%20%E9%81%8B%E7%AE%97%E5%AD%90%20Operator%20e3d81e9586904e1a9ed2f3df2719dcf0/Ex10.py)

## Ex.11 有一間學校共有n位新生，每k位一班，請製作一個程式輸入n,k值後輸出班級數及未分到班級的學生數

```python
n = int(input('n'))
k = int(input('k'))
print('班級數 =', n // k, '剩餘', n % k, '人') 
```

[Ex11.py](Lesson%204%20%E9%81%8B%E7%AE%97%E5%AD%90%20Operator%20e3d81e9586904e1a9ed2f3df2719dcf0/Ex11.py)

## 二、邏輯運算子

邏輯運算子可以進行比較和聯集、交集等判斷，運算結果為布林值。

| **運算子** | **功能** |
| --- | --- |
| a == b | 相等 (一個等於代表定義，兩個才是相等) |
| a != b | 不相等 |
| a > b | a大於b |
| a < b | a小於b |
| a >= b | a大於或等於b |
| a <= b | a小於或等於b |
| a and b | a且b (布林值運算) |
| a or b | a或b (布林值運算) |

### (1)等號的意義:

在python中，若使用一個等號為定義，例如定義變數。使用兩個等號為比較是否相同。

```python
x = 10 #定義x為10
x == 10 #判斷x是否等於10
```

### (2)布林值運算: and、or

布林值的運算符號**and(且)**、**or(或)**，也就是聯集與交集。簡易的計算方法為**由左到右，有括號先算，and需要左右皆為True才是True，or左右有一個為True即是True，沒有負負得正**

```python
#and
True and True => True
True and False => False
False and True => False
False and False => False
#or
True or True => True
True or False =>True
False or True => True
False or False => False
```

## Ex.12 試著計算以下的結果

```python
True or False and True
False and False or True
True or False and True and False or True and False or True and True
1 == '1' or 1 >= 1 and False or True
```

[Ex12.py](Lesson%204%20%E9%81%8B%E7%AE%97%E5%AD%90%20Operator%20e3d81e9586904e1a9ed2f3df2719dcf0/Ex12.py)

## 三、字串運算

字串的運算只有相加(+)、乘以整數，相加運算結果為兩個字串頭尾相接，乘以整數運算結果為重複字串。

```python
s1 = 'hello'
s2 = 'hi'
print(s1+s2)
```

```python
s1 = 'hi'
print(s1*2)
```

## Ex.13 獲取使用者名稱輸出: ‘嗨, 使用者名稱’

```python
print('hi '+input('pls enter ur name'))
```

[Ex13.py](Lesson%204%20%E9%81%8B%E7%AE%97%E5%AD%90%20Operator%20e3d81e9586904e1a9ed2f3df2719dcf0/Ex13.py)

## 四、串列運算

串列和字串相同，可以進行相加、乘以整數兩種運算，相加結果為兩個串列相接，乘以整數結果為重複串列中的內容。

```python
l1 = [123]
l2 = [456]
print(l1+l2)
```

```python
l1 = [123]
print(l1*2)
```

# 💯重點複習

### 運算子就是代表特定運算方法的符號，例如數學中的加減乘除

### 數學運算子算出結果為數字，邏輯運算子算出結果為布林值

### 字串、串列只有相加、乘以整數的運算方法

# 🏋️課後練習

## Q4:輸入兩個整數a,b，輸出相加、相減、相乘、相除、a的b次方

```python
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
```

[Q4.py](Lesson%204%20%E9%81%8B%E7%AE%97%E5%AD%90%20Operator%20e3d81e9586904e1a9ed2f3df2719dcf0/Q4.py)

---

### 💣課後延伸：

[Lesson 4-延伸  複合運算子](https://www.notion.so/Lesson-4-b114cb629b6249c5ae8d739efbe75831?pvs=21)