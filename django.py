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

# runserverを起動してみよう。(python manage.py runserver)
index_dict['runserverを起動してみよう。(python manage.py runserver)'] = (
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

# Profileモデルを作成していく。(app -> models.py)
index_dict['Profileモデルを作成していく。(app -> models.py)'] = (
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
1. ターミナルにて『 python manage.py makemigrations 』を実行する。
- Djangoにモデルに変更があったことを伝え、変更を マイグレーション の形で保存する。

2. ターミナルにて『 python manage.py migrate 』を実行する。
- mysite/settings.py ファイルのデータベース設定に従って必要なすべてのデータベースのテーブルを作成

```
python manage.py makemigrations
```

![](https://user-images.githubusercontent.com/79512367/123385516-95ea3480-d5d0-11eb-9ef0-1e6f053d4877.png)

#### ターミナルにて『 python manage.py migrate 』を実行する。
```
python manage.py migrate
```
![](https://user-images.githubusercontent.com/79512367/123386275-71428c80-d5d1-11eb-804a-3794bd72b659.png)

    """
)

# 管理ユーザーを作成する。(python manage.py createsuperuser)
index_dict['管理ユーザーを作成する。(python manage.py createsuperuser)'] = (
    """

## 管理ユーザーの情報を登録していく。
1. ターミナルにて『 python manage.py createsuperuser 』を実行する。
```
python manage.py createsuperuser
```

- 管理ユーザーのデータを入力していきます。
    - ユーザー名
    - メールアドレス
    - パスワード
    - パスワードの再入力

![](https://user-images.githubusercontent.com/79512367/123543445-70ecf180-d789-11eb-8aa1-ec092e8b3b69.png)

⚠️ パスワードは入力しても表示されませんが、
ちゃんと判断してくれるので間違えないように!!

    """
)

# 管理画面を開いてみる。 (URLに /adminを追加)
index_dict['管理画面を開いてみる。 (URLに /adminを追加)'] = (
    """

#### まずは、サーバーを起動する。(python manage.py runserver)
```
python manage.py runserver
```

URLの欄にて、URLの後ろに/admin を追加して管理画面に移動する。

![](https://user-images.githubusercontent.com/79512367/123547216-deede480-d79a-11eb-815f-45d0934c0415.png)

### この画面がDjangoの管理画面!!

![](https://user-images.githubusercontent.com/79512367/123548066-3f325580-d79e-11eb-838b-bfad5dad2a9b.png)

### ユーザー名とパスワードを入力して 【Django管理画面】に入る。

![](https://user-images.githubusercontent.com/79512367/123557903-77ea2300-d7ce-11eb-8cf7-d461c8e919cf.png)


    """
)

# Django管理画面でProfile(プロフィール)を追加する。
index_dict['Django管理画面でProfile(プロフィール)を追加する。'] = (
    """

### Django管理画面にてプロフィール情報を登録していく。
1.画面左上 APP欄のProfilesを選択。

![](https://user-images.githubusercontent.com/79512367/123558133-c51ac480-d7cf-11eb-9fd5-df36a37eda2f.png)

2.画面右上 PROFILEを追加 を選択。

![](https://user-images.githubusercontent.com/79512367/123558353-b254bf80-d7d0-11eb-8d8a-2a4daad2bdaf.png)

3.Djangoで作成したプロフィールモデルで入力画面が作成されている。
- 内容を入力していく。
- 入力が終われば、画面右下の『 保存 』を選択。

![](https://user-images.githubusercontent.com/79512367/123558593-11670400-d7d2-11eb-9a0b-2a9c29435f84.png)

4.Profileが追加されればOK!!

![](https://user-images.githubusercontent.com/79512367/123558808-30b26100-d7d3-11eb-8dd3-7543e1b8c953.png)

#### 修正したい場合は、修正したいprofileを選択したらできる!!

    """
)

# プロジェクトURLの設定を行う。(mysite -> urls.py)
index_dict['プロジェクトURLの設定を行う。(mysite -> urls.py)'] = (
    """

1. mysite -> urls.py を開く。

![](https://user-images.githubusercontent.com/79512367/123560365-a242dd00-d7dc-11eb-93a6-283ef1c02c96.png)

2. コードを追加していく。

```python
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

![](https://user-images.githubusercontent.com/79512367/125179932-cbc52500-e22e-11eb-822b-e4929071e271.png)
コードの意味は、わしにはわからん!!

    """
)

# アプリケーションURLの作成･設定を行う。(app -> urls.pyを新規作成)
index_dict['アプリケーションURLの作成･設定を行う。(app -> urls.pyを新規作成)'] = (
    """

1. appフォルダ -> urls.py を新規で作成する。

![](https://user-images.githubusercontent.com/79512367/123965727-b3b00300-d9ef-11eb-815d-527f18ef0ac1.png)


2. コードを追加していく。

![](https://user-images.githubusercontent.com/79512367/123967785-9a0fbb00-d9f1-11eb-9ce0-429f5d9ea6c8.png)

```python
from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

```

コードの意味は、わしにはわからん!!

    """
)

# トップページ用のビューを作成していく。(app -> views.py)
index_dict['トップページ用のビューを作成していく。(app -> views.py)'] = (
    """

1. app -> views.py を開く。

![](https://user-images.githubusercontent.com/79512367/123968442-2de18700-d9f2-11eb-9d46-c467fde2bbee.png)


2. コードを追加していく。

![](https://user-images.githubusercontent.com/79512367/124034560-555a4300-da36-11eb-8796-f0ccdda012a5.png)

```python
from django.http import request
from django.shortcuts import render
from django.views.generic import View
from .models import Profile


# Create your views here.
class IndexView(View):
    def get(self, reqest, **args, **kwargs):
        # 全てのプロフィールデータを取得
        profile_data = Profile.objects.all()
        # もしプロフィールデータがあるなら
        if profile_data.exists():
            # idを降順に並び替えて、最新のプロフィールデータを取得
            profile_data = profile_data.order_by('-id')[0]
        # プロフィールデータをindex.htmlに渡します。
        return render(request, 'app/index.html', {
            'profile_data': profile_data
        })

```

    """
)

# テンプレートフォルダーを作成しhtmlを作成する。(app -> templates -> app -> base.html)
index_dict['テンプレートフォルダーを作成しhtmlを作成する。(app -> templates -> app -> base.html)'] = (
    """

1. app -> templatesフォルダーを新規で作成する。
2. 作成したtemplatesフォルダーにappフォルダーを新規で作成する。
3. 新規で作成した appフォルダーにbase.htmlを作成する。

![](https://user-images.githubusercontent.com/79512367/124035944-3b216480-da38-11eb-97ba-a5828379b0a9.png)


4. base.html にコードを追加していく。

- Bootstrap 4 ドキュメントからCSSを読み込む。↓↓ URL ↓↓

https://getbootstrap.jp/docs/4.3/getting-started/introduction/

- Font Awesome のアイコンを使用するのにCSSを読み込む　↓↓ URL ↓↓

https://cdnjs.com/libraries/font-awesome

5. HTMLのコードを記載していく。

```
{% load static %}

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <title>ポートフォリオ</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a href="" class="navbar-brand">
                <img src="{% static 'img/logo.svg' %}" alt="" width="80" heght="80">
            </a>
            <ul class="navbar-nav">
                <li class="nav-item mr-3">
                    <a href="/" class="nav-link nav-color">HOME</a>
                </li>
                <li class="nav-item mr-3">
                    <a href="/" class="nav-link nav-color">ABOUT</a>
                </li>
                <li class="nav-item">
                    <a href="/" class="nav-link nav-color">CONTACT</a>
                </li>
            </ul>
        </div>
    </nav>

    <main>
        <div class="container">
        {% block content %}
        {% endblock %}
        </div>
    </main>

    <footer class="py-4 bg-dark text-center">
        <small class="text-white">&copy; 2021 赤嶺 龍弥 </small>
    </footer>

    {% block extra_js %}
    {% endblock %}


</body>
</html>

```
- HTMLの型は、! + Tab で呼び出して来れる。

![](https://user-images.githubusercontent.com/79512367/124038833-c3a20400-da3c-11eb-947e-8edc6016d6ac.png)

    """
)

# 動的に変わるhtmlを作成する。(app -> templates -> app -> index.html)
index_dict['動的に変わるhtmlを作成する。(app -> templates -> app -> index.html)'] = (
    """

1. templates -> appフォルダーに index.html を新規で作成する。

![](https://user-images.githubusercontent.com/79512367/124192218-e47f5d80-daff-11eb-8470-2f903fe7a32a.png)


2. HTMLのコードを記載していく。

```
{% extends 'app/base.html' %}

{% block content %}
<div class="card top d-flex flex-column justify-content-end mb-4">
    <img src="{{ profile_data.topimage.url }}" alt="">
    <div class="overlay text-white p-5">
        <h1 class="title">{{ profile_data.title}}</h1>
        <h5 class="subtitle">{{ profile_data.subtitle}}</h5>
    </div>
</div>

{% endblock  %}
```

![](https://user-images.githubusercontent.com/79512367/125140398-5f262980-e14d-11eb-90a1-6c5ba0b07626.png)


    """
)

# CSSファイルを作成する。(app -> static -> css -> style.css)
index_dict['CSSファイルを作成する。(app -> static -> css -> style.css)'] = (
    """

1. appフォルダーに新規でファイルを作成する。
- staticフォルダーを新規で作成。
- staticフォルダー内にcssフォルダーを作成。
- cssフォルダー内にstyle.cssファイルを作成。

![](https://user-images.githubusercontent.com/79512367/125149311-4b8db980-e173-11eb-9e65-2fe1acf151c1.png)

2. CSSのコードを記載していく。(誤入力もあるはず写真は後で撮ろう)

```
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    background: #f1f1f1;
    display: flex;
    flex-flow: column;
    min-height: 100vh;
}

main{
    flex: 1;
}

.navbar-nav{
    flex-direction: row!important;
}

.nav-color{
    color: black;
}

.nav-color:hover{
    color: #ee7c4d;
}

.nav-color::after{
    content: "";
    display: block;
    height: 2px;
    background: #EE6c4d;
    margin-top: 6px;
    opacity: 0;
    transform: translateY(12px);
    transition: all 0.3s ease-in-out;
}

.nav-color:hover:after{
    transform: translateY(0px);
    opacity: 1;
}

.top img {
    object-fit: cover;
    height: 500px;
}

.overlay{
    position: absolute;
}

.title{
    font-size: 2rem;
}

.subtitle {
    font-size: 2rem;
}
```
    """
)

# imgフォルダー(ロゴで使う)を作成する。(app -> static -> img)
index_dict['imgフォルダー(イメージフォルダー)を作成する。(app -> static -> img)'] = (
    """

1. app -> staticフォルダーに imgフォルダーを新規で作成する。

![](https://user-images.githubusercontent.com/79512367/125165649-d0f48680-e1d2-11eb-826f-58aa3406ee6b.png)

2. ロゴを表示するためにこの手順が必要。

![](https://user-images.githubusercontent.com/79512367/125166695-b8d33600-e1d7-11eb-95e5-2acefa4be4fc.png)

    """
)

# Workモデルを作成・adminに追加まで。(app -> models.py)
index_dict['Workモデルを作成していく。(app -> models.py)'] = (
    """

1. Workモデルを作成していく。

```python
# ワークモデルの作成。
class Work(models.Model):
    title = models.CharField('タイトル',max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    skill = models.CharField('スキル', max_length=100)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    created = models.DateField('作成日')
    description = models.TextField('説明')

    def __str__(self):
        return self.title

```

![](https://user-images.githubusercontent.com/79512367/125179920-a33d2b00-e22e-11eb-904e-3388076ac91f.png)


2. 追加したWorkモデルをadminに追加していく。
```python
from django.contrib import admin
from .models import Profile, Work

# Register your models here.
admin.site.register(Profile)
admin.site.register(Work)
```

![](https://user-images.githubusercontent.com/79512367/125179829-4bea8b00-e22d-11eb-9ed0-1f221f71d36b.png)

3. モデルを変更したのでマイグレーションを必要になります。
- ターミナルにて、下記コードを実行する。
```
python manage.py makemigrations
```
- 実行が終わると、ターミナルにて再度下記を実行。
```
python manage.py migrate
```
![](https://user-images.githubusercontent.com/79512367/125179902-6113e980-e22e-11eb-85d9-58f2a7f03cea.png)

4. Webサーバーを起動させて確認してみよう！
- ターミナルにて、下記を実行する。
```
python manage.py runserver
```
5. URLにアクセスし、URLに/adminを追加して管理画面にアクセスする。

![](https://user-images.githubusercontent.com/79512367/125265919-42057c80-e340-11eb-8b40-b79a12c55e08.png)

6. Django管理サイト画面から Works を追加していく。

![](https://user-images.githubusercontent.com/79512367/125266692-08814100-e341-11eb-8a1d-e763263cecca.png)

- こんな感じで４つほど追加してみよう!

![](https://user-images.githubusercontent.com/79512367/125267366-affe7380-e341-11eb-94a4-5edca3af7322.png)

    """
)

# Workデータをビューできるようにする。(app -> views.py)
index_dict['Workデータをビューできるようにする。(app -> views.py)'] = (
    """

1. app -> views.py にコードを追加していく。
- クラスのIndexView にコードを追加する。
```python
# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        # 全てのプロフィールデータを取得
        profile_data = Profile.objects.all()
        # もしプロフィールデータがあるなら
        if profile_data.exists():
            # idを降順に並び替えて、最新のプロフィールデータを取得
            profile_data = profile_data.order_by('-id')[0]
        work_data = Work.objects.order_by('-id')
        # プロフィールデータをindex.htmlに渡します。
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })
```
![](https://user-images.githubusercontent.com/79512367/125269380-99591c00-e343-11eb-99a8-83dae7e00708.png)

1. app -> templates -> index.html にコードを追加していく。
```
<div class="row mb-5">
    {% for work in work_data %}
        <div class="col-6 col-md-3 mb-3">
            <div class="card work-thumnail">
                {% if work.thumbnail %}
                    <img src="{{ work.thumbnail.url}}" alt="" class="work-img">
                {% else %}
                    <img src="{{ work.image.url}}" alt="" class="work-img">
                {% endif %}
                <div class="work-title text-centher">
                    <p class="mb-0">
                        {{ work.title }}
                    </p>
                </div>
                <a href="" class="stretched-link work"></a>
            </div>
        </div>
    {% endfor %}
</div>

{% endblock %}
```
![](https://user-images.githubusercontent.com/79512367/125282388-4dfa3a00-e352-11eb-9281-fe71dbbd96f4.png)

3. static -> css -> style.css にコードを追加していく。
```
.work-thumbnail {
    overflow: hidden;
    position: relative;
}

.work-img{
    object-fit: cover;
    height: 240px;
}

.work-title{
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
    color: white;
    font-weight: bold;
    padding: 10px 15px;
    opacity: 0;
    background-color: rgb(238, 108, 77, 0.8);
    transform: translateY(70px);
    transition: all 0.2s ease-in-out;
}

.work-thumbnail:hover .work-title{
    transform: translateY(0px);
    opacity: 1;
}

```
![](https://user-images.githubusercontent.com/79512367/125290582-6fabef00-e35b-11eb-8141-7e2e1b4efce5.png)

4. runserverを起動して状態を確認しよう！
- ターミナルにて、
```
python manage.py runserver
```


    """
)

# 作品詳細を見れるようにしていく。
index_dict['作品詳細を見れるようにしていく。'] = (
    """

1. app -> urls.py にコードを追加していく。
```
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
]
```

![](https://user-images.githubusercontent.com/79512367/126053393-32f4f0c9-0f79-446a-887c-ce8a44b585b4.png)

2. app -> views.py にコードを追加していく。

```
class DetailView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'work_data': work_data
        })


```

![](https://user-images.githubusercontent.com/79512367/126053432-ffd30e89-22d0-410e-8abb-752f277761a7.png)

3. templates -> app -> index.html を開きコードを追加していく。

- URLのdetail/<int:pk>/の<int:pkにwork.idが入る。

![](https://user-images.githubusercontent.com/79512367/126053591-e7ef01ea-e4b1-4326-a340-041093a63d84.png)

3. templates -> app -> に新規でファイルを作成し detail.html とする。

```
{% extends 'app/base.html' %}

{% block  content %}

<h3 class="mb-4">{{ work_data.title}}</h3>
<div class="card top mb-4">
    <img src="{{ work_data.image.url }}" alt="">
</div>

<div class="row">
    <div class="col-sm-4 mb-4">
        <h4 class="mb-3">INFORMATION</h4>
        <p>
            <i class="fas fa-laptop-code mr-2"></i>
            <span class="font-weight-bolder">SKILLS:</span>
            {{ work_data.skill}}
        </p>
        <hr>
        <p>
            <i class="fab fa-github mr-2"></i>
            <span class="font-weight-bolder">GITHUB:</span>
            {% if work_data.url %}
                <a href="{{ work_data.url }}" target="_blank" class="link-color">Link</a>
            {% else %}
                Privete
            {% endif %}
        </p>
        <hr>
        <p>
            <i class="fas fa-calendar-alt mr-2"></i>
            <span class="font-weight-bolder">CREATED:</span>
            {{ work_data.created}}
        </p>
        <hr>
    </div>
    <div class="col-sm-8 mb-5">
        <h4 class="mb-3">PROJECT DESCRIPTION</h4>
        <P>{{ work_data.description|linebreaksbr }}</P>
    </div>
</div>

{% endblock  %}
```

4. static -> css -> style.css を開きコードを追加していく。

    """
)

# プロフィール詳細/学歴･職歴を見れるようにしていく。
index_dict['プロフィール詳細/学歴･職歴を見れるようにしていく。'] = (
    """

1. app -> urls.py にコードを追加していく。

```
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('about', views.AboutView.as_view(), name='about'),
]

```
![](https://user-images.githubusercontent.com/79512367/126575570-42627513-333f-49ee-8c3b-8b918a72ad51.png)

2. app -> views.py にコードを追加していく。
- 下記コードを追加
```
class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        return render(request, 'app/about.html', {
            'profile_data': profile_data
        })

```

![](https://user-images.githubusercontent.com/79512367/126575741-40ee72d5-b84e-402b-8997-bc9ede36b3e5.png)

3. templates -> app -> base.html にコードを追加。

- ABOUT ボタンを押されると URLにabout を追加している。

![](https://user-images.githubusercontent.com/79512367/126576889-e7ebf919-92d8-4370-9406-9c1d20037521.png)

4. templates -> app -> about.html ファイルを新規で作成する。
- htmlのコードを記載していく。

```
{% extends 'app/base.html' %}

{% block content %}

<h3 class="mb-4">Profile</h3>
<div class="mb-5">
    <div class="row">
        <div class="col-md-8">
            <p>{{ profile_data.introduction|linebreaksbr }}</p>
        </div>
        <div class="col-md-4">
            <div class="card text-center px-5 py-4">
                <div class="avatar mb-3">
                    <img src="{{ profile_data.subimage.url}}" alt="" class="card-img-top rounded-circle">
                </div>
                <h5 class="font-weight-bolder">{{ profile_data.name}}</h5>
                <p class="mb-3 small text-center">{{ profile_data.job|linebreaksbr}}</p>
                <div class="d-flex justify-content-around">
                    {% if profile_data.github %}
                        <a href="{{ profile_data.github}}" target="_blank"><i class="fab fa-github fa-lg rounded btn-dark icon"></i></a>
                    {% endif %}
                    {% if profile_data.twitter %}
                        <a href="{{ profile_data.twitter}}" target="_blank"><i class="fab fa-twitter fa-lg rounded btn-primary icon"></i></a>
                    {% endif %}
                    {% if profile_data.lindedin %}
                        <a href="{{ profile_data.lindedin}}" target="_blank"><i class="fab fa-linded-in fa-lg rounded btn-info icon"></i></a>
                    {% endif %}
                    {% if profile_data.facebook %}
                        <a href="{{ profile_data.facebook}}" target="_blank"><i class="fab fa-facebook-f fa-lg rounded btn-dark icon"></i></a>
                    {% endif %}
                    {% if profile_data.instagram %}
                        <a href="{{ profile_data.instagram}}" target="_blank"><i class="fab fa-instagram fa-lg rounded btn-danger icon"></i></a>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>


{% endblock  %}

```

5. static -> css -> style.css を編集していく。

```
.abater img {
    max-width: 150px;
    max-height: 150px;
}

.icon {
    padding: 10px 8px;
}
```

![](https://user-images.githubusercontent.com/79512367/126578247-bb265d15-7659-420c-8521-9eec1c5d38ae.png)

6. 職歴･学歴のモデルを作っていく。
- app -> models.py にコードを追加していく。

```
# 職歴のモデルを作る。
class Exprience(models.Model):
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self) -> str:
        return self.occupation


# 学歴モデルを作る。
class Education(models.Model):
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self) -> str:
        return self.course

```

7. 管理画面でデータを登録できるようにしていく。

- app -> admin.py にコードを追加していく。

```
from django.contrib import admin
from .models import Profile, Work, Experience, Education

# Register your models here.
admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
```

![](https://user-images.githubusercontent.com/79512367/126593480-ec22c1cb-ee67-48a1-8a8c-0157bf639c37.png)

7. モデルを変更したので、マイグレーションを実行していく。(データベースの再構築)
- 『ターミナル』にて!

```
python manage.py makemigrations
```

- 処理が済んだら、『ターミナル』にて

```
python manage.py migrate
```

- 再構築が済んだので、webサーバーを起動させる。
```
python manage.py runserver
```

8. URLに『/admin』を追加してデータを入力していく。

![](https://user-images.githubusercontent.com/79512367/126594523-aed32d02-0c72-448f-8532-c9578e26286e.png)

9. app -> views.py にコードを追加していく。

- 追加したクラスモデルをimportする。

```
from django.shortcuts import render
from django.views.generic import View
from .models import Profile, Work, Experience, Education
```
![](https://user-images.githubusercontent.com/79512367/126608571-6e9153a6-9fb4-487b-8792-5de1e9beaea9.png) 


- AboutViewクラスに コードを追加していく。

```
class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        experience_data = Experience.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        return render(request, 'app/about.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data': education_data
        })

```
![](https://user-images.githubusercontent.com/79512367/126608578-3481ba5f-3c22-41fb-81c2-89ebeab8e9f6.png)

10. templates -> app -> about.html ファイルにコードを追加していく。

- about.html の{% endblock %} のすぐ上に追加する。

```

<h3 class="mb-4">Experience</h3>
<div class="mb-5">
    {% for experience in experience_data %}
        <div class="d-flex justify-content-between">
            <h5>{{ experience.occupation }} <span class="small text-secondary"> - {{ experience.company }}</span></h5>
            <p class="mb-1">{{ experience.period }}</p>
        </div>
        <p class="mb-1">{{ experience.description|linebreaksbr }}</p>
        <p>{{ experience.place }}</p>
        <hr>
    {% endfor %}
</div>

<h3 class="mb-4">Education</h3>
<div class="mb-5">
    {% for education in education_data %}
        <div class="d-flex justify-content-between">
            <h5>{{ education.course }} <span class="small text-secondary"> - {{ education.school }}</span></h5>
            <p class="mb-1">{{ education.period }}</p>
        </div>
        <p>{{ education.place }}</p>
        <hr>
    {% endfor %}
</div>

```

11. webサーバーを起動してみよう!!

- 『ターミナル』にて

```
python manage.py runserver
```

- ABOUTを選択してページを移動しよう!! 下記のような形になっていたらOK!!

![](https://user-images.githubusercontent.com/79512367/126612099-9ab5e764-a5ea-4ff8-b25b-6e72c8e1d7bb.png)

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
