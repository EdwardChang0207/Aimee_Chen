# Lesson 9 串列 List

Status: Done
課程進度: L9

# ❓Section I. 什麼是串列-List

串列(List)是一種python中的變數型態(Data Type)，串列(list)在其他程式語言中又叫做陣列(array)，串列(list)就像是一列火車，每個車廂可以**儲存任意資料型態(string, int, bool, list)**的不同資料，依據車廂的位置編號(index)，我們可以將資料取出使用，**串列的位置編號(index)會從0開始(第一個位置為0號位)，使用中括號"[]”即可宣告一個串列(list)**

## 一、建立串列

建立串列如同使用變數一樣，先定義串列的命名，等號右邊則使用中括號，每個值中間用逗號隔開

```python
list1 = [data1, data2, data3, ..., dataN]
```

## Ex.18 建立一個串列，包含1~10的數字並輸出

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
```

[Ex18.py](Lesson%209%20%E4%B8%B2%E5%88%97%20List%20e59be956b4ab48c091c9ed20b2d72079/Ex18.py)

# ⚙️Section II. 串列應用

## 一、空串列

空串列就是一個裡面**沒有任何資料**的串列，若不確定該串列中會有幾個資料時，就可以先宣告一個空串列。

## Ex.19 建立一個空串列並輸出

```python
list1 = []
print(list1)
```

[Ex19.py](Lesson%209%20%E4%B8%B2%E5%88%97%20List%20e59be956b4ab48c091c9ed20b2d72079/Ex19.py)

## 二、串列取值

**list_name[index] ⇒ 取得陣列中指定位置的值，其中位置從0開始**

```python
list1 = [1, 2, 3, 4]
print(list1[2])
```

## Ex.20 建立裝有1~10的串列分別取出4、7

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[3], list[6])
```

[Ex20.py](Lesson%209%20%E4%B8%B2%E5%88%97%20List%20e59be956b4ab48c091c9ed20b2d72079/Ex20.py)

## 三、串列長度

**取得串列長度: len(list_name)**

```python
list1 = [1, 2, 3, 4]
print(len(list1))
```

## 四、串列函式(Function)

通常用於取得串列資訊。不會影響串列的內容，要求串列作為參數（parameter）。

| 函式 Function_name | 功能 Function |
| --- | --- |
| len(list_name) | 取得串列長度 |
| max(list_name) | 取得串列中的最大值 |
| min(list_name) | 取得串列中的最小值 |
| sum(list_name) | 取得指定串列值的綜合 |
| tuple(list_name) | 將串列轉換為元組 |
|  |  |

## Ex.21 在一個裝有1~10的串列中求最大值、最小值、總和

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(list1), min(list1), sum(list1))
```

[Ex21.py](Lesson%209%20%E4%B8%B2%E5%88%97%20List%20e59be956b4ab48c091c9ed20b2d72079/Ex21.py)

## 五、串列方法(Method)

串列方法可以改變串列中的內容，例如增建串列項目、改變順序等。

| 方法 Method | 功能 Function |
| --- | --- |
| list.append(element) | 在串列最後加入元素 |
| list.count(element) | 計算某元素在串列中的數量 |
| list.index(element) | 尋找某元素在串列中的位置 |
| list.insert(position, element) | 在串列中的指定位置加入元素 |
| list.pop() | 移除串列中最後一個元素 |
| list.remove(element) | 移除串列中指定的元素 |
| list.reverse() | 反轉串列所有元素的位置 |
| del list_name[start: end: interval] | 刪除指定範圍的元素 |
| list.sort() | 重新排序(改變原串列) |
| list.sorted() | 重新排序(建立新串列) |

## Ex.22 將裝有1~10的串列反轉後刪除最後一項

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.reverse()
list1.pop()
print(list1)
```

[Ex22.py](Lesson%209%20%E4%B8%B2%E5%88%97%20List%20e59be956b4ab48c091c9ed20b2d72079/Ex22.py)

## 六、多維串列

多維串列可以想像成在串列中還有串列，所以程式碼若展開大致如下：

```python
2d_list = [
	[a, b, c],
	[d, e, f],
	[g, h, i]
]
```

若我們想要從多維串列中取值，我們需要依照串列的層次指定位置：

```python
2d_list = [
	[a, b, c], #0
	[d, e, f], #1
	[g, h, i]. #2
  #0 #1 #2
]
print(2d_list[0][2])
```

因為如此的特性，在應用上常常會當作遊戲地圖做使用

# 💯重點複習

### **串列(list)就像是一列火車，每個車廂可以儲存任意資料型態(string, int, bool, list)的不同資料，依據車廂的位置編號(index)，我們可以將資料取出使用**

### 串列位置從0開始算起

### 串列函式不會改變原串列內容，串列方法會改變原串列內容

# 🏋️課後練習

## Q8: 在以下串列(list1)中新增12,13,15並排續，再將串列反轉，刪除第4項和最後一項後輸出最大值、最小值、總和、平均

```python
list1 = [24, 54, 12, 56, 78, 89]
```

[Q8.py](Lesson%209%20%E4%B8%B2%E5%88%97%20List%20e59be956b4ab48c091c9ed20b2d72079/Q8.py)