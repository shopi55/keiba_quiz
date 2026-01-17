from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# レース情報テーブルの定義
class KQT_101(db.Model): #db.Model を使うことで「データベースのテーブル」として扱える
  __tablename__ = "KQT101" #DB上で扱うテーブル名の指定（指定しない場合、モデル名を小文字したものがテーブル名となる）
  race_id = db.Column(db.Integer,primary_key=True,autoincrement=True) #カラムの定義
  race_date = db.Column(db.Date, nullable=False) # 年と月をまとめて格納
#  year = db.Column(db.Integer,nullable=False)
#  month = db.Column(db.Integer,nullable=False)
  race_name = db.Column(db.String,nullable=False)
  results = db.relationship('KQT_301', backref='race') # ('クラス名', 相手側クラスにある属性名) クラス間で親子関係が誕生

# 馬情報テーブルの定義
class KQT_201(db.Model):
  __tablename__ = "KQT201"
  horse_id = db.Column(db.Integer,primary_key = True,autoincrement=True)
  # horse_name = db.Column(db.String,nullable=False, unique=True)
  horse_name = db.Column(db.String,nullable=False)
  results = db.relationship('KQT_301', backref='horse')

# 馬番着順テーブルの定義
class KQT_301(db.Model):
  __tablename__ = "KQT301"
  result_id = db.Column(db.Integer,primary_key = True,autoincrement=True)
  race_id = db.Column(db.Integer,db.ForeignKey('KQT101.race_id'),nullable=False)
  horse_id = db.Column(db.Integer,db.ForeignKey('KQT201.horse_id'),nullable=False)
  waku_number = db.Column(db.Integer,nullable=False)
  horse_number = db.Column(db.Integer,nullable=False)
  ranking_id = db.Column(db.Integer,nullable=False)
