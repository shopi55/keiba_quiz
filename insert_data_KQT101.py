# 数十～数百MB程度のcsvの場合に実施

import pandas as pd
import sqlite3

# CSVの読み込み
df = pd.read_csv('sample_data/sample_KQT101.csv')

# SQLiteに指定したテーブル名で保存
with sqlite3.connect('keiba_quiz.db') as conn:
    df.to_sql('KQT101', conn, if_exists='replace', index=False)

print('データ追加完了！')