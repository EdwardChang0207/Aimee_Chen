# Lesson 12 意外處理 try&except

Status: Done

# Section 1. 什麼是意外處理

在先前的課程中，我們的程式都是需要先規劃好輸入及處理程序，但在實際的應用中，我們常會遇到使用者輸入意外的內容，例如：

```python
x = input('請輸入整數')
print( int(x) + 1 )
```

若使用者輸入的內容不是整數，如：’hello’則程式就會出現錯誤後終止執行。

為了預防該狀況，我們可以先使用意外處理的方式，告訴程式遇到錯誤時，該如何反應。

# Section 2. Try & except

為了預防上面所述的情況，我們可以使用try及except告訴程式，遇到錯誤時該怎麼處理，方法如下：

```python
try: #可能會出錯的區塊
	x = input('請輸入整數')
	print( int(x) + 1 )
except: #如果出錯的處理的方式
	print('錯誤！輸入的不是整數!)
```

在try區塊中，我們會放入可能會出錯的程式區塊，若該區塊出現錯誤，則會執行except

# Section 3. 錯誤類別

程式碼出錯時，我們可能會希望對不同的錯誤進行不同的處理方式，以下是常見的錯誤類別：

| 錯誤資訊 | 說明 |
| --- | --- |
| NameError | 使用沒有被定義的對象 |
| IndexError | 索引值超過了序列的大小 |
| TypeError | 數據類型 ( type ) 錯誤 |
| SyntaxError | Python 語法規則錯誤 |
| ValueError | 傳入值錯誤 |
| KeyboardInterrupt | 當程式被手動強制中止 |
| AssertionError | 程式 asset 後面的條件不成立 |
| KeyError | 鍵發生錯誤 |
| ZeroDivisionError | 除以 0 |
| AttributeError | 使用不存在的屬性 |
| IndentationError | Python 語法錯誤 ( 沒有對齊 ) |
| IOError | Input/output異常 |
| UnboundLocalError | 區域變數和全域變數發生重複或錯誤 |

當我們想要針對不同錯誤類別進行處理時，我們就可以將類別名稱寫在except後方：

```python
try: #可能會出錯的區塊
	x = input('請輸入整數')
	print( int(x) + 1 )
except TypeError: #如果出錯的處理的方式
	print('錯誤！輸入的不是整數!)
except IOError #如果出錯的處理的方式
	print('錯誤！請輸入內容!)
```