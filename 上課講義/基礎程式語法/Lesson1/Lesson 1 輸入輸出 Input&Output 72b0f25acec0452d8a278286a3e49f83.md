# Lesson 1 輸入輸出 Input&Output

Status: Done
課程進度: L1

<aside>
💡 改動請註解於command

</aside>

<aside>
💡 學習指標: print()、input()基礎使用

</aside>

# ❓Section I. 什麼是程式

我們可以**把程式想像成一個機器**，在寫程式的過程，我們就是在**設計一台機器**。

![input.png](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/input.png)

每個機器都會有自己需要的**原料(輸入)、特定的功能和指定的產品(輸出)**，得到指定的原料後，經過機器程序，便可以得到目標的輸出內容。

# ⬆️Section II. 輸入、輸出函式

## 一、輸出函式 print(輸出內容)

使用輸出函式可以讓電腦輸出指定的內容。

```python
print(輸出內容)
```

### (1)輸出文字

若要輸出一段文字，我們需要先標註這段內容是文字，使用**引號{’’、””}**，即可標註文字

```jsx
'這是一段文字'
"這是一段文字"
```

### **Ex1**: 使用print()輸出HelloWorld

```python
print('HelloWorld') #文字需使用''或""
```

[Ex1.py](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/Ex1.py)

### (2)輸出數字

因為電腦已經認識數字，所以我們不需要再特別標註數字

```python
123
456
3.14
```

### **Ex1-1**: 使用print()輸出123

```python
print(123)
```

[ex1-1.py](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/ex1-1.py)

### (3)輸出算數結果

python可以直接幫我們完成數學運算，只需直接print()算式就會印出結果

### **Ex1-2**: 使用print()輸出123+456的答案

```python
print(123+456)
```

[ex1-2.py](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/ex1-2.py)

### (4)輸出多個內容

python可以使用一個print()輸出複數個內容，只需在各個輸出內容間使用**逗號**隔開

### **Ex1-3**: 使用print()輸出123、早安

```python
print(123,'早安')
```

[ex1-3.py](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/ex1-3.py)

### (5)分隔符號 sep

做完ex1-3後，我們發現兩個輸出內容之間會被**空格**隔開，原因是print()的預設分隔符號是**空格**，我們可以手動更改分隔符號，只需使用sep參數即可

```python
print(123, 456, sep='分隔符號'）
```

### **Ex1-4**: 使用print()輸出1~5，中間使用逗號隔開

```python
print(1, 2, 3, 4, 5, sep=',')
```

[ex1-4.py](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/ex1-4.py)

### (6)結尾符號 end

在開始說明結尾符號前，我們可以先觀察以下程式碼：

```python
print(123)
print(456)
```

輸出後，我們可以發現兩行輸出自動換行了，原因是在每一個print()的結尾，print()會幫我們加入一個結尾符號，預設的結尾符號為“**換行**”，換行字元為“**\n**”

## 二、輸入函式 input(’提示字元’)

使用輸入函式可以讓程式獲得使用者輸入的內容，提示字元用來要求使用者輸入指定內容，例如:請輸入帳號。

### (1)獲取輸入

```python
input('提示字元')
```

使用者輸入的內容會直接替代該函式的位置，若想要將內容再輸出出來則可以直接將input()放入print()中

```python
print(input())
```

### **Ex2**: 輸入一串文字並讓程式輸出該文字

```python
print(input())
```

[Ex2.py](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/Ex2.py)

### (2)輸入分割 .split(‘分割符號’)

若我們獲取的同一行輸入中有多個資訊，我們可以使用**split()**將其分割，預設以空格作為分割點

```python
input().split() #將輸入內容從空格分割
```

若我們檢視分割後的結果，我們將會得到一個**串列(List)**，在L2會詳細介紹

# 💯重點複習

### 使用print()可以在terminal輸出想要的內容，使用逗號可以一次輸出多個內容

```python
print(輸出內容1,輸出內容2,...)
```

### 在多個輸出內容之間，會使用間隔符號隔開，使用sep參數可以指定間隔符號

```python
print(輸出內容1,輸出內容2,...,sep='間隔符號')
```

### 輸出最後會加上一個結尾符號，可以使用end參數指定結尾符號

```python
print(輸出內容,end='結尾符號')
```

### 間隔符號預設為“空格”、結尾符號預設為“\n”(換行)

### 使用input()可以獲得使用者在terminal輸入的內容，獲得的值會直接取代函式本身的位置，在括號內可以輸入提示字串，提示使用者應該輸入的內容

```python
input('提示字串')
```

### 使用split()即可將輸入的內容分隔，其中可以使用分割符號參數指定分割點

```python
input().split('分割符號')
```

# 🏋️課後練習

## Q1: 詢問使用者的名字後輸出使用者的名字

參考解答:

[Q1.py](Lesson%201%20%E8%BC%B8%E5%85%A5%E8%BC%B8%E5%87%BA%20Input&Output%2072b0f25acec0452d8a278286a3e49f83/Q1.py)

# ✏️習題練習

- [ZeroJudge a001](https://zerojudge.tw/ShowProblem?problemid=a001)
    
    **參考解答：**
    
    ```python
    print('hello', input())
    ```
    

---

### 課後延伸：

[Lesson 1 延伸-連續輸入](https://www.notion.so/Lesson-1-062fe215b0704ae6b66b0dacd35b7298?pvs=21)