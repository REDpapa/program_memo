"""
このtemplate.pyの中身をコピーして
サイト構築をしていこう!!

streamlit_web.py ファイルを開いて、
1. sidebar_list リストにファイル名を追加する
2. import で自作ファイルを読み出す

"""

# 最初に辞書型を定義
index_dict = {}

# ******このエリアにindex_dict[] = を書いていく********************

# MySQLサーバーを起動と停止
index_dict['MySQLサーバーを起動と停止'] = (
    """
1. MySQLを起動する
- ターミナルにて
```
mysql.server start
```
![](https://user-images.githubusercontent.com/79512367/129416463-c54ef26d-1a3c-43a8-aaf3-135b135c7746.png)

2. MySQLを停止させる。
```
mysql.server stop
```
![](https://user-images.githubusercontent.com/79512367/129416670-71315a33-9c94-4842-81f6-6032267eb5ac.png)

    """
)

# MySQLサーバーにログイン/プロジェクトの作成/ログアウト
index_dict['MySQLサーバーにログイン/プロジェクトの作成/ログアウト'] = (
    """
1. MySQLにログインする。
- MySQLサーバーを起動しておく。
- 最初はこのコマンドで入れる。
- パスワード設定が完了している場合はエラーが出る。
```
mysql -u root
```

2. パスワード設定が終わっている場合のログイン。
```
mysql -u root -p
```
![](https://user-images.githubusercontent.com/79512367/129417462-53c55afb-8a28-4bf1-a778-b74b84257048.png)

3. MySQLサーバーを起動せずにログインした場合のエラー

![](https://user-images.githubusercontent.com/79512367/129417706-fe75c427-5193-42e8-99f9-091c6077882a.png)


4. プロジェクトの作成
```
create database <プロジェクト名>;
```
![](https://user-images.githubusercontent.com/79512367/129420414-ca982548-6929-47e9-822b-bdf5655e852c.png)

5. MySQL からログアウトする。
```
exit
```
byeと表示される!!
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
    # text_send('type() 型を確認する')