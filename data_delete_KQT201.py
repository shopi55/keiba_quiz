import sqlite3

# データベースへの接続
conn = sqlite3.connect('keiba_quiz.db')

# カーソルの作成
# カーソルはSQL文をデータベースに送信して実行するためのオブジェクト
cursor = conn.cursor()

cursor.execute('DELETE FROM KQT201')

conn.commit()

print('削除が完了しました')