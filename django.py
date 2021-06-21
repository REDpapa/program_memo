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
```
pip install -r requirements.txt
```
![](https://user-images.githubusercontent.com/79512367/122568921-36969c80-d085-11eb-8815-3eccc6cf83d8.png)
    """
)

# プロジェクトの作成(django-admin startproject mysite .)
index_dict['プロジェクトの作成(django-admin startproject mysite .)'] = (
    """
#### プロジェクトの作成
```
django-admin startproject mysite .
```

![](https://user-images.githubusercontent.com/79512367/122824259-6363e180-d31b-11eb-9efd-9ba512c80d01.png)

#### 作業ディレクトリに『mysite』ディレクトリが作成される

![](https://user-images.githubusercontent.com/79512367/122824991-4e3b8280-d31c-11eb-8307-2ab502578334.png)
    """
)

# settings.py にて、言語設定と時間設定を変更する
index_dict['settings.py にて、言語設定と時間設定を変更する'] = (
    """
#### mysite -> settings.py を開く \nLANGUAGE_CODE と TIME_ZONE の設定を変更する

![](https://user-images.githubusercontent.com/79512367/122827105-edfa1000-d31e-11eb-8c41-c96cfb1233b9.png)

![](https://user-images.githubusercontent.com/79512367/122827110-ef2b3d00-d31e-11eb-8608-50dbcf7d3282.png)

#### 日本語で東京の時間に設定したことです。
    """

)

# 画像をアップロードするファイルを指定
index_dict['画像をアップロードするファイルを指定'] = (
    """
#### mysite -> settings.py 末端にコードを追加する。

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
![](https://user-images.githubusercontent.com/79512367/122829695-4848a000-d322-11eb-97b7-7e20eaf524ea.png)

#### os ライブラリーのimprotができていないので追加

```python
import os
```
![](https://user-images.githubusercontent.com/79512367/122830624-8f836080-d323-11eb-9983-b4d5791fdf2a.png)    """

)

# データベースを構築する(migrate)
index_dict['データベースを構築する(migrate)'] = (
    """
#### ターミナルにて『 python manage.py migrate 』を実行する

```
python manage.py migrate
```
![](https://user-images.githubusercontent.com/79512367/122831208-7fb84c00-d324-11eb-9323-030602b276df.png)

#### 作業ディレクトリに db.sqlite3 のデータベースが作成される。
![](https://user-images.githubusercontent.com/79512367/122831808-6368df00-d325-11eb-89c1-c871eb088bda.png)
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
