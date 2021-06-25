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
### 再起動などで再度始める際は、アクティベイト操作をして仮想環境に入ろう!
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

# runserverを起動してみよう。
index_dict['runserverを起動してみよう。'] = (
    """
#### ターミナルにて『 python manage.py runserver 』を実行する。
#### 囲いの中のURLに『 command + クリック 』でアクセスする。

```
python manage.py runserver
```
![](https://user-images.githubusercontent.com/79512367/123351381-f27d2d80-d597-11eb-92b7-787146ec0b57.png)


#### アクセス先がこのような画面になれば、問題ありません!!
![](https://user-images.githubusercontent.com/79512367/123351763-d62dc080-d598-11eb-9483-f7953e5bb376.png)
    """
)

# runserverを終了してみよう。
index_dict['runserverを終了してみよう。(control + c)'] = (
    """
#### ターミナルの画面にて『 control + c 』を押す。これだけ!

![](https://user-images.githubusercontent.com/79512367/123352138-a337fc80-d599-11eb-90dd-72478487da93.png)

#### ※ runserverを終了させたので、URLのアクセス先がアクセスできなくなります。

![](https://user-images.githubusercontent.com/79512367/123352462-49840200-d59a-11eb-9091-77d7e50e2113.png)
    """
)

# アプリケーションを作成してみよう。(python manage.py startapp app)
index_dict['アプリケーションを作成してみよう。(python manage.py startapp app)'] = (
    """
#### ターミナルの画面にて『 python manage.py startapp app 』を実行。
作業フォルダーに、app(アプリケーション)をいうフォルダーが追加される。

```
python manage.py startapp app
```

![](https://user-images.githubusercontent.com/79512367/123356975-b5b73380-d5a3-11eb-8bcf-db8273821ab0.png)

    """
)

# アプリケーションを使えるよに設定を変更する。(settings.py の INSTALLED_APPSに追加)
index_dict['アプリケーションを使えるよに設定を変更する。(settings.py の INSTALLED_APPSに追加)'] = (
    """
#### settings.pyファイルの 環境変数 INSTALLED_APPS にアプリを追加する作業をする。
1. app 作成したアプリケーションを追加
2. widget_tweaks フォーム画面を作る時に便利なので追加

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',  # ここの部分を追加
    'app',  # ここの部分を追加
]
```

![](https://user-images.githubusercontent.com/79512367/123370199-33863980-d5ba-11eb-9a17-62aef6be18bc.png)

    """
)

# モデルを作成していく。(app -> models.py)
index_dict['モデルを作成していく。(app -> models.py)'] = (
    """
#### appフォルダのmodels.pyファイルを開き作業していく。
1. appフォルダ -> models.pyファイル を開く。
2. Profile(プロフィール)のモデルクラスを作成する。

作業ファイルはここ!!
![](https://user-images.githubusercontent.com/79512367/123371775-52d29600-d5bd-11eb-9232-249dedda2643.png)


#### app -> models.py にプロフィール用のコードを入力。


```python
class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name
```

![](https://user-images.githubusercontent.com/79512367/123373534-7ea34b00-d5c0-11eb-9c78-2590cb246dcd.png)

    """
)

# 管理画面の作成を行う。(app -> admin.py)
index_dict['管理画面の作成を行う。(app -> admin.py)'] = (
    """

## 管理画面を作成して、データを登録できるようにする。

#### appフォルダのadmin.pyファイルを開き作業していく。
1. appフォルダ -> admin.pyファイル を開く。
2. models.py で作成した Profile クラスを呼び出してくるコードを作成。


#### 作業ファイルはここ!!

![](https://user-images.githubusercontent.com/79512367/123382855-64239e80-d5cd-11eb-8f01-d2e333b33092.png)

#### models.py で作成した Profile クラスを呼び出してくるコードを作成。
追加するコードは、これ!!
#### admin の管理画面のモデルをProfileで作成しているイメージ

```python
from django.contrib import admin
from .models import Profile  # これを追加

# Register your models here.
admin.site.register(Profile)  # これを追加
```
![](https://user-images.githubusercontent.com/79512367/123383672-6a664a80-d5ce-11eb-9a38-21727a3a9aa0.png)

    """
)

# データベースを再構築する。(python manage.py makemigrations)
index_dict['データベースを再構築する。(python manage.py makemigrations)'] = (
    """

## モデルを追加したので、データベースの再構築をする。

#### ターミナルにて『 python manage.py makemigrations 』を実行する。


```
python manage.py makemigrations
```

#### こんな感じになれば OK!!

![](https://user-images.githubusercontent.com/79512367/123385516-95ea3480-d5d0-11eb-9ef0-1e6f053d4877.png)

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
