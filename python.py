"""
pythonの基本コードをここに！
追加項目があるたびにテンプレに従うようにしたい。
"""

# 最初に辞書型を定義
index_dict = {}

# ******このエリアにindex_dict[] = """コード"""を書いていく********************
index_dict['type() 型を確認する'] = """
# type() 型を確認する

num = 1
name = 'REDpapa'
is_ok = True

print(num,type(num))
print(name,type(name))
print(is_ok,type(is_ok))

-> 1 <class 'int'>
-> REDpapa <class 'str'>
-> True <class 'bool'>
"""

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