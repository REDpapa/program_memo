"""
辞書型定義で考えるのが面白いかも!?
{select内容:pythonコード,・・・}みたいな形で増やしていくのわどうよ！？
"""


# インポートを行う。as dtとしてメソッドの呼び出しはdt.で行う。
from datetime import datetime as dt

# 現在日時を扱う。 時間秒まで。
present_time = dt.now()
print(present_time)

# 現在年月日を扱う。
current_date = dt.now().date()
print(current_date)

# 文字列をdate型に変更する。
d = dt.strptime('2021/04/21', '%Y/%m/%d').date()
print(d)
print(type(d))

# 今日の日付を取得する。datetime型とstr型yyyymmdd
# datetime型時間まで出るポイ
today_date = dt.today()
# str型yyyymmdd
today_date = dt.strftime(dt.today(), '%Y%m%d')


def index_send():
    index_list = [
        'datetime ライブラリーのインポート',
        '現在日時を扱う。 時間秒まで。',
        '現在年月日を扱う。',
        '現在年月日を扱う。',
    ]

    return index_list


def text_send(index_list):
    if index_list == 'datetime ライブラリーのインポート':
        text_send = (
            """
            # コメントテスト

            ```Python
            # komenntotes
            from datetime import datetime as dt
            ```
            """
            )

        return text_send


if __name__ == '__main__':
    index_send()
    text_send('datetime ライブラリーのインポート')
