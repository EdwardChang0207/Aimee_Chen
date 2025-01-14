# Lesson 2 變數 Variable

Status: Done
課程進度: L2

<aside>
💡 改動請註解於comment

</aside>

<aside>
💡 學習指標: 認識變數和基礎變數型態(int、float、string、bool)

</aside>

# 🏋️課前暖身

請完成以下題目：(10分鐘)

[自我介紹](https://www.notion.so/ca00afec00b643d6af430dbdde0fa834?pvs=21)

---

# ❓Section I. 什麼是變數

變數可以想像成一個箱子或是一個容器，可以將任意的資料儲存在其中，可以用數學的未知數想像，如下舉例。

## Ex.3 定義一個變數x其值為10，輸出x加10的結果。

```python
x = 10 #定義變數x的值為10
print(x+10) #輸出x加上10的結果
```

[Ex3.py](Lesson%202%20%E8%AE%8A%E6%95%B8%20Variable%2092b4c7dc531647eb9fe78bfcdcd6c374/Ex3.py)

從上面的例子，我們可以知道定義變數的方法為: “**變數名稱 = 值**”。變數除了可以放入數字之外，也可以放入文字。

## Ex.4 定義一個變數x其值為字串’Hello’，並輸出x的值。

```python
x = 'Hello'
print(x)
```

[Ex4.py](Lesson%202%20%E8%AE%8A%E6%95%B8%20Variable%2092b4c7dc531647eb9fe78bfcdcd6c374/Ex4.py)

# 🆎Section II. 變數型態 DataType

變數中可以儲存多種不同的資料，例如在Ex.3、Ex.4中，我們分別儲存了**數字**和**文字**，除此之外還有眾多的資料可以儲存在變數之中，這些不同的資料種類我們稱之為資料型態”**Data Type**”。

## 一、數字 Numbers

### (1)整數 Integer: 沒有小數點的數

在python中，所有沒有小數點的數字我們都稱為整數，簡寫為”**int**”。

```python
x = 10
y = 5
z = -1
```

### (2)浮點數 Float: 任何帶有小數點的數

在python中只要含有小數點的數字，就稱為浮點數，代號為”**float**”。

```python
x = 2.41
y = 3.141
z = 5.0 #注意!小數點後為0依然為浮點數!
```

## 二、文字 String

### (1)字串 String: 任意的文字、數字、符號都可被定義為字串

字串是所有變數型態中規定最為寬鬆的，任何的字元都可以被定義為字串，只要將資料放入**引號(’’&””)**中，程式就會判定其為字串，字串在程式中簡寫為”**str**”。

```python
x = 'hello'
y = '@'
z = '5.0' #注意"5.0"仍是字串，只要在引號中，該資料就是字串!
```

## 三、布林值 Booling

### (1)True(真)、False(假): 表達有與無的狀態

布林值只有兩個值True(真)與False(假)，用來表達有與無、開與關等兩種狀態間的切換，就是電腦1和0的概念，布林值在程式中簡寫為”**bool”。**

```python
x = True
y = False
```

## 四、串列 List

### (1)串列 List: 就像火車一樣的儲存資料

串列就像是一台火車，火車上有很多個車廂，不同車廂可以運送不同貨物。以程式來說那些貨物就是**不同的資料型態**。所以我們可以在**一個串列中放入多種不同資料型態的資料**，再藉由他的**位置**（車廂編號）抓取想要的資料。

若我們想建立一個串列，可以使用**中括號[]**，並將不同資料使用**逗號**隔開

```python
list1 = [v1,v2,v3,...]
```

## Ex.5 定義變數x為整數10，y為字串5.1，z為布林值True，將x、y、z放入串列l，並輸出xyz的值及l

```python
x = 10
y = '5.1'
z = True
l = [x,y,z]
print(x)
print(y)
print(z)
print(l)
```

[Ex5.py](Lesson%202%20%E8%AE%8A%E6%95%B8%20Variable%2092b4c7dc531647eb9fe78bfcdcd6c374/Ex5.py)

## 四、判斷變數型態 type(data)

使用type()可以得知資料的變數型態。

## Ex.6 判斷Ex.5中xyz的變數型態並使用print()輸出

```python
x = 10
y = '5.1'
z = True
l = [x,y,z]
print(type(x))
print(type(y))
print(type(z))
print(type(l))
```

[Ex6.py](Lesson%202%20%E8%AE%8A%E6%95%B8%20Variable%2092b4c7dc531647eb9fe78bfcdcd6c374/Ex6.py)

## 五、變數型態轉換

使用python中的內建函式即可將變數型態進行轉換。

```python
int() #轉為整數
float() #轉為浮點數
str() #轉為字串
bool() #轉為布林值
list() #轉為串列
```

# 💯重點複習

### 變數就好像容器或是箱子，也可以用數學中的未知數來想像。

### 定義一個變數⇒ 變數名稱 = 值

```python
variable_name = value
#ex. x = 10
```

### 程式中的變數除了像數學未知數可以放入數字之外，也可以放入其他資料，例如字串、布林值等。

### 變數中可以放入的不同資料種類稱為變數型態(Data Type)

### 基本的變數型態大致分為四類:

### 1.數字: 整數 integer(**int**)、浮點數 float(float)

### 2.文字: 字串 string(str) ⇒ 需放入引號中

### 3.布林值: True、False

### 4.串列: [v1,v2,v3,…]

### 使用type()可以得知該筆資料的變數型態(Data Type)

### 變數型態之間可以互相轉換，int()可轉為整數、float()可轉為浮點數、str()可轉為字串、bool()可轉為布林值

# 🏋️課後練習

[應聲蟲](https://www.notion.so/d2e7771b1ba747d694f07027e5f64cae?pvs=21)

[使用者資料整理](https://www.notion.so/562a4b94e09d44d4ac0f84e5dcb2513f?pvs=21)

---

### 課後延伸：

[Lesson 2 延伸-定義多個變數](https://www.notion.so/Lesson-2-3a1f78ba763d4393b11682e85bf76b63?pvs=21)

[Lesson 2 延伸-變數命名](https://www.notion.so/Lesson-2-699b5dbec7e74e31bdfe7315ee0ec284?pvs=21)