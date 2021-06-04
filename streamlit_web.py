"""
streamlit を使ってwebサイトを作ってみる。
設計図イメージは、左側のサイドバーにて表示したいメモを選択すると
メイン画面にプログラムのメモを表示する仕組みにしたい。
"""

# 必要ライブラリーのインポート
from PIL import Image
import streamlit as st

# 自作ファイルの読み出し
import date_time

# *********ここからwebサイトに表示される***********************

# ***********サイドバーを表示していく!***********************

image = Image.open('Twitterアイコン.jpg')
# img データを表示する。caption=は画像名　use_column_width=Trueは、表示するブラウザに合わせる。
st.sidebar.image(image, caption='REDpapaイメージ', use_column_width=True)

st.sidebar.text('見たいものを選択してください')
option_check_0 = st.sidebar.checkbox('python')
option_check_1 = st.sidebar.checkbox('anaconda')
option_check_2 = st.sidebar.checkbox('GitHub')
option_check_3 = st.sidebar.checkbox('gspread')
option_check_4 = st.sidebar.checkbox('LINE_BOT')
option_check_5 = st.sidebar.checkbox('pipenv')
option_check_6 = st.sidebar.checkbox('仮想環境')
option_check_7 = st.sidebar.checkbox('pandas')
option_check_8 = st.sidebar.checkbox('ローカル定期実行')
option_check_9 = st.sidebar.checkbox('日付と時間')

# ***********メインを表示していく!***********************

st.header('REDpapaのプログラムメモ')
st.text('左のサイドバーより見たい項目をチェックしてください!')

if option_check_9:
    st.text('日付と時間を表示')
    index_list = date_time.index_send()

    option_select = st.selectbox(
        'どれか一つを選択してください',
        index_list
    )
    st.write('あなたが選んだのは', option_select)
    st.write(date_time.text_send(option_select))
