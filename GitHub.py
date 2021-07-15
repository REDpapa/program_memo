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

# GitHub にフォルダーを公開する手順
index_dict['GitHub にフォルダーを公開する手順'] = (
    """
1. GitHub のサイトにアクセスする。
- https://github.com/
2. 左上の『New』の緑ボタンにて、Repository(リポジトリ)を作成画面に移動する。
![](https://user-images.githubusercontent.com/79512367/125775691-aab0a03f-c9e3-4a7d-830c-ddc3e961cc48.png)
3. Repository name を決めて入力する。(やることがわかる内容がいいかも)
- このサイトを利用して、リポジトリ名を決めるといい!!
- https://codic.jp/engine
4. Public(公開)かPrivate(非公開)を選択する。


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
