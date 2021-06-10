"""
streamlit を使ってwebサイトを作ってみる。
設計図イメージは、左側のサイドバーにて表示したいメモを選択すると
メイン画面にプログラムのメモを表示する仕組みにしたい。
"""

# 必要ライブラリーのインポート
from PIL import Image
import streamlit as st

# 自作ファイルの読み出し
import python
import date_time


# *********ここからwebサイトに表示される***********************

# //////////////サイドバーを表示していく!////////////////////////////

image = Image.open('./image/Twitterアイコン.jpg')
# img データを表示する。caption=は画像名　use_column_width=Trueは、表示するブラウザに合わせる。
st.sidebar.image(image, caption='REDpapaイメージ', use_column_width=True)

st.sidebar.header('見たいものを選択してください')

# サイドバーに選択リストを表示する!⭐️リスト名=ファイル名⭐️になるようにする。
sidebar_list = [
    'python',
    'date_time',
    # 'gspread',
    # 'pandas'
]
# sidebar_listの数だけサイドバーにチェックリストを作成する。
sidebar_check_list = [st.sidebar.checkbox(_) for _ in sidebar_list]

# /////////////////////////////////////////////////////////////////////////

# ***********メインを表示していく!***********************

st.header('REDpapaのプログラムメモ')
st.text('左のサイドバーより見たい項目をチェックしてください!')

# サイドバーのチェックリストがTrueのものがあれば、メイン画面に表示!
for i, sidebar_bool in enumerate(sidebar_check_list):
    if sidebar_bool:
        st.header(f'{sidebar_list[i]}を表示')
        selectbox_list = eval(f'{sidebar_list[i]}.index_send()')
        # セレクトBOXを表示する。
        option_select = st.selectbox(
            'どれか一つを選択してください',
            (selectbox_list)
        )

        # セレクトBOXで選択されたものを引数に、参考コードを呼び出す。
        # NOTE:eval()メソッドは、文字列をpythonコードとして判断してくれる！
        st.markdown(
            eval(f'{sidebar_list[i]}.text_send(option_select)'),
            )

# *****************************************************************
