"""
pythonの基本コードをここに！
追加項目があるたびにテンプレに従うようにしたい。
"""

# 最初に辞書型を定義
index_dict = {}

# ******このエリアにindex_dict[] = """コード,出力結果"""を書いていく********************
# type() 型を確認する
index_dict['type() 型を確認する'] = (
    """
```python
# type() 型を確認する

num = 1
name = 'REDpapa'
is_ok = True

print(num,type(num))
print(name,type(name))
print(is_ok,type(is_ok))
```
#### 出力結果
```bash
1 <class 'int'>
REDpapa <class 'str'>
True <class 'bool'>
```
    """
)

# 辞書からキーを指定して値を取得する。
index_dict['辞書からキーを指定して値を取得する。'] = (
    """
```python
# 辞書からキーを指定して値を取得する。
mydict = {"JP": "Japan", "DE": "Germany", "FR": "France"}

print(mydict["JP"])
print(mydict["DE"])
print(mydict["FR"])
```
#### 出力結果
```bash
Japan
Germany
France
```
    """
)

# リスト内の値を結合する。
index_dict['リスト内の値を結合する。'] = (
    """
```python
# リスト内の値を結合する。
list = ['A', 'B', 'C']

print(''.join(list))
print(','.join(list))
```
#### 出力結果
```bash
ABC
A,B,C
```
    """
)

# リスト内の値を結合する。(要素に数値型が含まれる場合)
index_dict['リスト内の値を結合する。(要素に数値型が含まれる場合)'] = (
    """
```python
# リスト内の値を結合する。(要素に数値型が含まれる場合)
list = ['A', 'B', 'C', 1, 2, 3]

map = map(str, list)

print(''.join(map))
```
#### 出力結果
```bash
ABC123
```
    """
)

# ************************************************************

index_keys_list = list(index_dict.keys())


# index_send関数
def index_send():
    """
    この関数を呼び出すと、
    このファイル内の出力可能なindex_listを返してくる。
    """
    return index_keys_list


# text_send関数
def text_send(index_keys_set):
    """
    この関数が呼び出されると、
    pythonコードのマークダウンが出力される!!
    """
    return index_dict[index_keys_set]


if __name__ == '__main__':
    index_send()
    text_send('type() 型を確認する')
