"""
このファイルは、REDpapaが困ったことをやって書いて行こう!

"""

# 最初に辞書型を定義
index_dict = {}

# ******このエリアにindex_dict[] = を書いていく********************

# フォルダー内に見た目では、存在しないファイルが存在している。(.DS_Store)
index_dict['フォルダー内に見た目では、存在しないファイルが存在している。(.DS_Store)'] = (
    """
### PILを使うのにフォルダからファイルをimgデータを読み出すとこんな異常が出た。
##### PIL.UnidentifiedImageError: cannot identify image file 'img/.DS_Store'
翻訳内容:画像ファイルを識別できません 'img / .DS_Store

- 問題点は、imgフォルダに『 .DS_Store 』なんて存在しないのに読み込まれている。
- 『 .DS_Store 』は邪魔なので消してやりたいが、見た目に存在しないからどうするの？
![](https://user-images.githubusercontent.com/79512367/123541130-cae7ba00-d77d-11eb-9be3-0b9f053202db.png)


### 解決策 と 手順
1. まずは、異常のあるフォルダに移動してみよう!!
- ターミナルにて『 cd 異常のあるフォルダー』で作業フォルダを移動しよう!
```
cd img
```

2. 『 .DS_Store 』が存在するのか確認してみよう
- ターミナルにて『 find . -name ".DS_Store 』で.DS_Storeの存在を確認して
```
find . -name ".DS_Store
```

3.『 .DS_Store 』が存在したのなら、実際に削除してこう!!
- ターミナルにて『 find . -name ".DS_Store" | xargs rm 』を実行する。
```
find . -name ".DS_Store" | xargs rm
```

4. 2項のコマンドを再度実行して『 .DS_Store 』が存在しなくなっていたらOK!!
```
find . -name ".DS_Store
```
![](https://user-images.githubusercontent.com/79512367/123541991-18febc80-d782-11eb-87ea-e021b28cf406.png)

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
