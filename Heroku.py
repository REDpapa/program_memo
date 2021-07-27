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

# Heroku 参考にした動画・記事のURLをおく。
index_dict['参考にした動画・記事のURLをおく。'] = (
    """
1. Herokuのドキュメントページ

https://devcenter.heroku.com/ja/articles/getting-started-with-python?singlepage=true

2. 参考にしたUdemyの動画(有料)

https://www.udemy.com/course/python-web-api/learn/lecture/25663396#content

3. 定期実行の方法などがわかる動画

https://www.youtube.com/watch?v=u-qrnpq7OOE&t=3173s

4. Heroku に環境変数を設定する方法

https://lotus-base.com/blog/19

5. Heroku のコマンドのメモ

https://qiita.com/nao_h/items/91bcfbdd1d558bff6dc0


    """
)


# Heroku を使う準備をする。
index_dict['Heroku を使う準備をする。'] = (
    """
1. Heroku のWebサイトにアクセスして、アカウントの作成を行う。

https://dashboard.heroku.com/apps

2. Heroku CLI をインストールする。
- ホームブリューでインストールできる。(僕は、何を言われてるか意味わかってない)
- 僕は、Pythonの師匠に教えてもらいながらやったところ・・・
- 下記のURLからインストールできるので頑張れ!!

https://devcenter.heroku.com/ja/articles/heroku-cli
```
brew tap heroku/brew && brew install heroku
```

3. 参考にしたUdemyの動画
https://www.udemy.com/course/python-web-api/learn/lecture/25663396#content

    """
)

# Herokuへ、リモート実行環境を構築していく。
index_dict['Herokuへ、リモート実行環境を構築していく。'] = (
    """
1. Heroku へデプロイするフォルダー内に『Procfile』ファイルを新規で作成する。
- この『Procfile』内にHerokuで実行する内容を記載していく場所。

![](https://user-images.githubusercontent.com/79512367/126857807-703e9a67-84ad-4b95-9c74-19be1b61bd35.png)

- 実行して欲しいコードを記載する。下記コードは、pythonのwoeker.py ファイルを実行しての意味

```
worker: python worker.py
```

2. 『requirements.txt』をファイルを新規で作成する。
- requirements.txt には必要な外部ライブラリーを記載する。

![](https://user-images.githubusercontent.com/79512367/126859195-36069624-1819-4c5c-82ff-ca8132449188.png)


    """
)

# Heroku へ 新しいプログラムをデプロイする。
index_dict['Heroku へ 新しいプログラムをデプロイする。'] = (
    """
1. Heroku へログインしていく。

- 『ターミナル』にて
- (HerokuのCLIがインストールができていること)

```
heroku login
```

- 実行するとこんな感じになる。-> enterを押す!!

![](https://user-images.githubusercontent.com/79512367/126859351-7ecfd2d8-0d8f-42c2-9c40-04a04bba20c1.png)

- ブラウザが立ち上がるので、Log Inのボタンを押す!!

![](https://user-images.githubusercontent.com/79512367/126859414-0909ee9e-f3ec-48db-9992-b33ed7fd530d.png)

- ログイン完了したらこんな感じになる。

![](https://user-images.githubusercontent.com/79512367/126859552-618d32b9-320c-44bb-8c8a-06baa3fb0269.png)

2. Heroku にデプロイするアプリケーション名を決める。

- heroku create ここにアプリケーション名 (Heroku上で固有の名前じゃないとだめ!!)
- アンダーバーは使えないぽい!ので注意して!!
- 『ターミナル』にて
```
heroku create ここにアプリケーション名
```
- 成功すると下記の画像のようになる!!

![](https://user-images.githubusercontent.com/79512367/126859882-6693f2bb-9df1-422a-a003-f280ec270f3b.png)

- Heroku のWebサイトにアクセス(開いていたらリロード)でアプリケーションが追加されいるはず。

![](https://user-images.githubusercontent.com/79512367/126860138-686292f2-2418-4096-b520-ecd3bd444919.png)

3. GitHubと紐付けを行っていく!!

- まずは、Gitの初期化　『ターミナル』にて
```
git init
```

- gitとherokuの紐付け　『ターミナル』にて
- heroku git:remote -a アプリケーション名で行う。
```
heroku git:remote -a アプリケーション名
```

- これでgitとherokuの紐付けが済んでます。下記コードで確認できる。
```
git remote -v
```
![](https://user-images.githubusercontent.com/79512367/126860421-b1c47529-47f8-4590-81ec-d4e1870d3ba0.png)

- 後はGitHubのpushとほぼ同じ!!『ターミナルにて』
##### 全てのファイルを選択して。
```
git add .
```
- コミットメッセージを入れて。
#### メッセージ内容はなんだっていいよ!
```
git commit -m 'heroku 1com'
```

- 『 git remote app heroku アプリケーションURL 』を実行してherokuのアプリケーションURLを指定する。
- アプリケーションURLの確認方法は『 git remote -v 』で確認できる。

```
git remote app heroku アプリケーションURL
```

- 『 git push heroku master 』を実行することで、herokuにデプロイが開始される。
```
git push heroku master
```
##### ※ちょっと時間かかるけど気にしないで!!

- デプロイが完了したら、再度HerokuのWebサイトにアクセスしてリロードしよう!!
下記画像のようにPythonと理解してくれていたらOKでしょう!!

![](https://user-images.githubusercontent.com/79512367/126861099-113ac7f6-e268-4ebd-bcc5-2b853f3ea0ea.png)

    """
)

# Heroku へ プログラムの変更したものをデプロイする。(アプリケーション作成済み)
index_dict['Heroku へ プログラムの変更したものをデプロイする。(アプリケーション作成済み)'] = (
    """
1. Heroku へログインしていく。

- 『ターミナル』にて

```
heroku login
```

- 実行するとこんな感じになる。-> enterを押す!!

![](https://user-images.githubusercontent.com/79512367/126859351-7ecfd2d8-0d8f-42c2-9c40-04a04bba20c1.png)

- ブラウザが立ち上がるので、Log Inのボタンを押す!!

![](https://user-images.githubusercontent.com/79512367/126859414-0909ee9e-f3ec-48db-9992-b33ed7fd530d.png)

- ログイン完了したらこんな感じになる。

![](https://user-images.githubusercontent.com/79512367/126859552-618d32b9-320c-44bb-8c8a-06baa3fb0269.png)

2. Heroku にデプロイしているアプリケーション名を調べる。

```
heroku apps
```
- 下記のような形でアプリケーションの確認ができる。

![](https://user-images.githubusercontent.com/79512367/127224913-1f5bb50b-4d68-4ba3-851c-a8037a054b7c.png)

3. アプリケーションの概要を確認して、git URLを確認していく。

```
$ heroku info --app <アプリケーション名>
```

- Git URLを確認する。

![](https://user-images.githubusercontent.com/79512367/127226809-4735ed05-4b47-43ce-89a4-6022ba52824f.png)

4. 後は、Gitのpush工程と同じ!!

全てのファイルを選択して
```
git add .
```

コミットメッセージを入れて

```
git commit -m 'コミットメッセージ'
```

pushしていく(アプリケーションのGit URLは、３項で確認したもの)

```
git push <アプリケーションのGit URL> master
```

これでOK!!(少し時間かかるけど)

    """
)

# Heroku Webサイト内でアプリケーションの設定をしていく。【常に実行しておく設定】
index_dict['# Heroku Webサイト内でアプリケーションの設定をしていく。【常に実行しておく設定】'] = (
    """
1. デプロイしたアプリケーションを選択する。

![](https://user-images.githubusercontent.com/79512367/126861201-d6eb6573-c3b1-4861-a3c9-828f90fd9dfb.png)

2. Dyno formation欄の右下が『OFF』になっているので切替えていく。
- Configure Dynos を選択する。

![](https://user-images.githubusercontent.com/79512367/126861299-66bcb820-0598-4d2c-9fb5-d5fe7b2916d9.png)

- えんぴつマークをクリックして。
![](https://user-images.githubusercontent.com/79512367/126861681-8e3419a5-d5cf-4734-a2a1-17c32b3c6978.png)
- バーをON(右に切替)して。
![](https://user-images.githubusercontent.com/79512367/126861683-e0c1c4cc-6494-47ee-a111-c20156b23441.png)
- Confirmをクリックする。
![](https://user-images.githubusercontent.com/79512367/126861685-ebd47897-55a6-438e-a76e-f4ae30d4b205.png)
- こうなったらOK!!
![](https://user-images.githubusercontent.com/79512367/126861686-021a8039-d6b9-4759-b64b-fb6a5ac4f755.png)
- タブの Overview をクリックして移動し、下記の画面のようになればOK!!
![](https://user-images.githubusercontent.com/79512367/126865627-782265ba-e81e-4d06-beaa-265e0208e0b1.png)

恐らくこれで常にプログラムが動いている状態だと思う!!

    """
)


# Heroku Webサイト内でアプリケーションの設定をしていく。【定期実行する設定】
index_dict['# Heroku Webサイト内でアプリケーションの設定をしていく。【定期実行する設定】'] = (
    """

### 参考にした記事
- https://qiita.com/nsuhara/items/fac20adb6b0a122a3709

1. デプロイしたアプリケーションを選択する。

2. タブの『Resources』をクリックし、紫のボタンの『Find more add-ons』をクリックする。

![](https://user-images.githubusercontent.com/79512367/126880066-ded190a3-dde4-42c3-9a88-e9723bfae539.png)

3. 下にスライドさせて行き、『 Heroku Scheduler 』を探しクリックする。

![](https://user-images.githubusercontent.com/79512367/126880563-2d6415f1-da11-4602-a2c4-775b4550ca5d.png)

4. 画面右上の『 Install Heroku Scheduler 』をクリックして、スケジュールアプリをインストールをする。

![](https://user-images.githubusercontent.com/79512367/126880564-0326c26f-36a8-4009-9f4c-271f072e5727.png)

5. App to provision to の入力欄に Herokuにデプロイしたアプリケーション名を入力し、Enterを押す。

![](https://user-images.githubusercontent.com/79512367/126880565-991755d3-5985-460f-8722-51528f1db0e0.png)

6. 下記のような画面になるので、『 Submit Order Form 』ボタンをクリックする。

![](https://user-images.githubusercontent.com/79512367/126880570-b006b417-d8ec-4da8-82e6-79c24c2e93b2.png)

7. Heroku Scheduler のアプリが追加されるので、追加されたアプリをクリックする。

![](https://user-images.githubusercontent.com/79512367/126880574-fe0f3ff2-e06b-4f21-869c-aa325f521d23.png)

8. 下記のような画面になるので『 Create job 』をクリックして、スケジュールの設定を開始する。

![](https://user-images.githubusercontent.com/79512367/126880576-ef34d326-de80-447d-b9e0-a5d470d25608.png)

9. Job Editor が立ち上がるので、下記の画像を参考に設定をしてください。

#### ※UTC時間での設定になるので、日本時間にするには９時間減算してください。
#### <例えば>　朝の6時に設定したいなら、UTC時間では22:00(PM10:00)にする。

![](https://user-images.githubusercontent.com/79512367/126880578-fdc29020-8067-4e8b-8879-e74e6a8821ca.png)

10. 設定は、これで完了です。下記のような画面になるので設定の確認をして見てください。
![](https://user-images.githubusercontent.com/79512367/126880581-486a6bef-7fbb-46ac-b225-70a883e37152.png)

## お疲れ様でした!!

    """
)

# ターミナルを使って Heroku でログを確認する。
index_dict['ターミナルを使って Heroku でログを確認する。'] = (
    """
1. まずは、Heroku にログインする。『ターミナル』にて！

```
heroku login
```
- 実行するとこんな感じになる。-> enterを押す!!

![](https://user-images.githubusercontent.com/79512367/126859351-7ecfd2d8-0d8f-42c2-9c40-04a04bba20c1.png)

2. ブラウザが立ち上がるので、Log Inのボタンを押す!!

![](https://user-images.githubusercontent.com/79512367/126859414-0909ee9e-f3ec-48db-9992-b33ed7fd530d.png)

- ログイン完了したらこんな感じになる。

![](https://user-images.githubusercontent.com/79512367/126859552-618d32b9-320c-44bb-8c8a-06baa3fb0269.png)

3. Heroku のログを表示する。『ターミナル』にて。

```
heroku logs
```

この手順でログの確認ができるはず!!


    """
)

# Heroku に環境変数を設定する。
index_dict['Heroku に環境変数を設定する。'] = (
    """

## 環境変数の設定方法は、２つ方法がある。

### １つ目ターミナルを使った方法!!


1. まずは、Herokuにログインする。

2. 『 heroku config:set 環境変数="アクセスキーなどなど" -a アプリケーション名 』 で設定できる。

<例えば>
- 環境変数名が "ACCESS_TOKEN"
- 環境変数の値が "abcde5963"
- アプリケーション名が "heroku-thanks"
であった場合は下記のようにターミナルで実行する。

```
heroku config:set ACCESS_TOKEN=abcde5963 -a heroku-thanks
```

- アプリケーション名はこんな感じで確認するといいと思う!!

![](https://user-images.githubusercontent.com/79512367/127055951-75d1c868-d7f4-41fb-a89a-13b1ba11ebda.png)

- コマンド入力時の注意点と成功の画像

![](https://user-images.githubusercontent.com/79512367/127057196-bc958a31-0ede-4bfd-866b-b99d102d1a4b.png)

### ２つ目 Heroku のWebサイトから環境変数を設定する。こっちの方がオススメ!!

1. Heroku Webサイトにアクセスして ログインする。

2. 環境変数を追加したい アプリケーションを選択。

3. タブの settings をクリックする。

![](https://user-images.githubusercontent.com/79512367/127058036-5778437c-7de1-40ab-a07b-29731a2cf9ee.png)

4. Config Vars 欄の Reveal Config Vars ボタンをクリックする。

![](https://user-images.githubusercontent.com/79512367/127058453-f29ef83d-fe69-4870-8eef-aa7276357885.png)

5. 『KEY』と『VALUE』を入力して、Addボタンをクリックする。ここで設定の確認もできる。

![](https://user-images.githubusercontent.com/79512367/127059237-a23e3ae2-25a9-45f4-a086-035b6a361723.png)

以上で終わりです!!

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