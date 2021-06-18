"""
pythonの基本コードをここに！
追加項目があるたびにテンプレに従うようにしたい。
"""

# 最初に辞書型を定義
index_dict = {}

# ******このエリアにindex_dict[] = """コード,出力結果"""を書いていく********************
# Django用のファイルを用意する。
index_dict['Django用のファイルを用意する。'] = (
    """
特にここは、問題なく作成できるでしょう。
画面左上が今回作成したファイル名です。
『DJANGO_MYPORTFOLIO』

![img_1](https://user-images.githubusercontent.com/79512367/122516677-067dd800-d04a-11eb-970b-502706656353.png)

    """
)

# 仮想環境の作成とアクティベイト(仮想環境内に入る)
index_dict['仮想環境の作成とアクティベイト(仮想環境内に入る)'] = (
    """
## ターミナルで実行
#### 仮想環境を作成　【myvenv】
```
python -m venv myvenv
```
#### 仮想環境にアクティベイト
```
source myvenv/bin/activate
```

![img_2](https://user-images.githubusercontent.com/79512367/122516501-d1718580-d049-11eb-8fda-dd3d5dd138ce.png)


#### こうなればOK!
```
(myvenv) ◆自分のパソコンのpath◆ django_myportfolio %
```
##### 再起動などで再度始める際は、アクティベイト操作をして仮想環境に入ろう!
    """


)

# requirements.txtを作成してライブラリーを管理する。
index_dict['requirements.txtを作成してライブラリーを管理する。'] = (
    """
#### 右クリックから新しいファイルを作成を選択しrequirements.txtにファイル名を変更する。
![](https://user-images.githubusercontent.com/79512367/122549614-a6992880-d06d-11eb-8f4d-de4fcf2d2f0d.png)

#### requirements.txt に必要ライブラリーをバージョンを指定して記載。
![](https://user-images.githubusercontent.com/79512367/122568244-85900200-d084-11eb-93a2-87f840e9dba0.png)

#### requirements.txt に記載されたライブラリーを元にライブラリーをinstallする。
![](https://user-images.githubusercontent.com/79512367/122568921-36969c80-d085-11eb-8815-3eccc6cf83d8.png)
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
