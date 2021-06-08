"""
pythonの基本コードをここに！
追加項目があるたびにテンプレに従うようにしたい。
"""

# 最初に辞書型を定義
index_dict = {}

# ******このエリアにindex_dict[] = """コード,出力結果"""を書いていく********************
# datetimeのインポートを行う。
index_dict['datetimeのインポートを行う。'] = (
    """
```python
# datetimeのインポートを行う。

from datetime import datetime as dt
```
#### asにてstを指定したので、メソッドの呼び出しはdt.で行う。
    """
)

# 現在の年月日時間を扱う。(today()差と同じ!?)
index_dict['現在の年月日時間を扱う。(today()差と同じ!?)'] = (
    """
```python
# 現在の年月日時間を扱う。
current_date_time = dt.now()

print(current_date_time)
print(type(current_date_time))
```
#### 出力結果
```bash
2021-06-07 05:37:33.589826
<class 'datetime.datetime'>
```
    """
)

# 現在の年月日までを扱う。
index_dict['現在の年月日までを扱う。'] = (
    """
```python
# 現在の年月日までを扱う。
current_date = dt.now().date()

print(current_date)
print(type(current_date))
```
#### 出力結果
```bash
2021-06-07
<class 'datetime.datetime'>
```
    """
)

# 文字列の年月日をdatetime型に変更する。
index_dict['文字列の年月日をdatetime型に変更する。'] = (
    """
```python
# 文字列の年月日をdatetime型に変更する。
date_str = '2021/04/21'
d = dt.strptime(date_str, '%Y/%m/%d').date()

print(d)
print(type(d))
```
#### 出力結果
```bash
2021-04-21
<class 'datetime.date'>
```
    """
)

# 今日の年月日･時間を取得する。
index_dict['今日の年月日･時間を取得する。'] = (
    """
```python
# 今日の年月日･時間を取得する。
today_date_time = dt.today()

print(today_date_time)
print(type(today_date_time))
```
#### 出力結果
```bash
2021-06-07 05:40:56.755774
<class 'datetime.datetime'>
```
    """
)

# 今日の年月日データをstr型でyyyymmddの形で取得する。
index_dict['今日の年月日データをstr型でyyyymmddの形で取得する。'] = (
    """
```python
# 今日の年月日データをstr型でyyyymmddの形で取得する。
today_date = dt.strftime(dt.today(), '%Y%m%d')

print(today_date)
print(type(today_date))
```
#### 出力結果
```bash
20210607
<class 'str'>
    """
)

# ************************************************************

# index_listのキーデータをリストにする。
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
