# Lesson 10 💾元組(Tuple)、📖字典(Dictionary)

Status: Done
課程進度: L10

# 🚆Section1. 元組

元組(Tuple)和串列(List)同樣都可以用於儲存複數筆資料，但是元組所存的資料不可被程式更動，因此元組只能使用函式(Function)不能使用方法(Method)，使用元組可以獲得比串列更快的執行速度。在先前的章節中，我們想像串列為一個火車，那如果將元組加入這個想像，串列就可以想像為自由座的火車，元組就可以想像為對號座的火車。建立一個元組與建立串列的方法相同，只要將”[]”替代為”()”即可。

```python
list1 = [1, 2, 3, 4] #建立一個串列
tuple1 = (1, 2, 3, 4) #建立一個元組
x = tuple1[0] #=> 1
```

### ⚙️元組函式

元組的函式與串列基本相同，只有記住元組不可使用方法(Method)即可。

| 函式 Function_name | 功能 Functions |
| --- | --- |
| len(tuple_name) | 取得串列長度 |
| max(tuple_name) | 取得串列中的最大值 |
| min(tuple_name) | 取得串列中的最小值 |
| sum(tuple_name) | 取得指定串列值的綜合 |
| list(tuple_name) | 將元組轉換為串列 |

# 📖字典(Dictionary)

字典與串列和元組相同也是儲存資料的方法，但是與前述兩者不同的是，字典(Dictionary)使用關鍵字(Key)當作尋找資料的方法，串列和元組則是使用資料儲存的位置(position)當作尋找資料的依據。建立字典有兩種方法，第一種(dict1)需使用”{}”，在鍵(Key)與值(Value)之前使用”:”隔開，資料與資料之間使用”,”分隔。第二種(dict2、dict3)則是使用dict()，如下所示。

```python
dict1 = {'John':30, 'Eddy':21, 'Mary':18} #建立一個字典
dict2 = dict(['John', 30], ['Eddy', 21], ['Mary',18])
dict3 = dict('John' = 30, 'Eddy' = 21, 'Mary' = 18)
```

## 👀字典取值

字典取值是以鍵(Key)當作索引值，程式寫法如下:

```python
dict1 = {'John':30, 'Eddy':21, 'Mary':18} #建立一個字典
dict1['John'] #=> 30
```

除了這種寫法之外也可使用字典的方法:”.get()”

```python
dict1 = {'John':30, 'Eddy':21, 'Mary':18} #建立一個字典
dict1.get('John') #=> 30
```

## ⚙️字典函式(精簡版)

| 函式 Function_name | 功能 Functions |
| --- | --- |
| len(dict_name) | 取得字典長度 |

## ♟️字典方法(精簡版)

| 函式 Function_name | 功能 Functions |
| --- | --- |
| dict.get(key, init) | 獲取字典中某項資料，如果不存在則返回init的值 |
| dict.keys() | 獲取字典中所有的key，返回串列 |