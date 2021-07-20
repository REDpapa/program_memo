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

# GitHub にフォルダーを公開する手順1(リポジトリの作成まで)
index_dict['GitHub にフォルダーを公開する手順1(リポジトリの作成まで)'] = (
    """
1. GitHub のサイトにアクセスする。

- https://github.com/
- ※アカウントがない場合は作成してください!!(ここはやり方覚えてない・・・)

2. 左上の『New』の緑ボタンにて、Repository(リポジトリ)を作成画面に移動する。

![](https://user-images.githubusercontent.com/79512367/125775691-aab0a03f-c9e3-4a7d-830c-ddc3e961cc48.png)

3. Repository name を決めて入力する。(やることがわかる内容がいいかも)

- このサイトを利用して、リポジトリ名を決めるといい!!

- https://codic.jp/engine

![](https://user-images.githubusercontent.com/79512367/125854189-07ae9225-16ac-4696-870a-486754e95a8b.png)

4. Public(公開)かPrivate(非公開)を選択する。

- Public(公開)にする場合は、シークレットキーやアクセストークンは公開しないように注意して!!

5. 下の方にある緑のボタン。『create repository』のボタンを押す。

![](https://user-images.githubusercontent.com/79512367/125854985-f97882fa-8a46-4c19-ad0d-08c28b8a6f72.png)

6. HTTPと書かれた後の部分をURLをコピーする。

- ※GitHubとフォルダを紐付けする時に使用する。

![](https://user-images.githubusercontent.com/79512367/125858127-ae050c88-a430-44bc-aeb8-ecee61a9fd96.png)
    """
)

# GitHub にフォルダーを公開する手順2(GitHubに公開完了まで)
index_dict['GitHub にフォルダーを公開する手順2(GitHubに公開完了まで)'] = (
    """
1. vscodeで公開したいフォルダーを開く。
- エディターはなんでも同じはず!ここではvs codeで行う。

2. 新しいターミナルを開き、公開するディレクトリに移動する。
- cd コマンドを使って移動してください!!下記URL参考になるはず
- https://qiita.com/ryouzi/items/f9dee1540a04a0bfb9a3

![](https://user-images.githubusercontent.com/79512367/125859762-c0398c53-3b0e-4be5-b600-cbe5c788a3ce.png)

3. GitHubの初期化　必ずするもの程度の考えでOK。

- 『ターミナルで!!』

```
git init
```

4. どのGitHubにリモートで紐付けるかの宣言。

- 『ターミナルで!!』

```
git remote add origin 手順1でコピーしたURL
```

5. ちゃんとGitHubに紐付いたか確認するイメージ。

- 『ターミナルで!!』

```
git remote -v
```

6. 全てのディレクトリと宣言。

- 『ターミナルで!!』

```
git add .
```

7. コミットするコメントを入力する。初めてのコミットなので'1st commit'

- 『ターミナルで!!』

```
git commit -m'1st commit'
```

8. GitHubにpushする。
　
- 『ターミナルで!!』

```
git push origin master
```

- 3 ~ 8項までの参考画像

![](https://user-images.githubusercontent.com/79512367/125955690-4c72c163-b62e-4f93-9eef-b2b0f7f7ddaa.png)

9. ブラウザのGitHubページを更新する。

![](https://user-images.githubusercontent.com/79512367/125956173-3355c868-7a96-4077-a6b8-1045a7d037bc.png)

10. こんな画面になっていたら、GitHubに公開完了。

![](https://user-images.githubusercontent.com/79512367/125956180-8509b03a-9b26-4158-95f7-181605707a81.png)

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
