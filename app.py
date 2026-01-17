from flask import Flask, request, render_template, redirect, url_for
import os

from models import db,KQT_101, KQT_201, KQT_301

app = Flask(__name__)

# --------------------------------------
# FlaskとDBの紐づけ
# --------------------------------------
base_dir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir,'keiba_quiz.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# --------------------------------------
# トップページ
# --------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# --------------------------------------
# 問題ページ
# --------------------------------------
@app.route('/quiz/<int:qid>',methods=['GET','POST'])
def quiz(qid):
    race = KQT_101.query.get(qid) # 主キーで1件取得
    if not race:
        return render_template(
            'end.html'
        )
    
    result = sorted(race.results, key=lambda r: r.horse_number)
    # ----------------------------------
    # 正解確認ページ
    # ----------------------------------
    if request.method == 'POST':
        # selected_horse_idは選んだ馬の馬番（horse_number）を持つ
        selected_horse_id = int(request.form.get('selected_horse')) # htmlのname要素selected_horseのvalue要素を取得
        # correct_resultはranking_idが「1」のhorse_id（FK）を持つ
        # race.resultは「SELECT * FROM KQT101 WHERE race_id = 1とか２など;」の意味を持つ
        correct_result = next(r for r in race.results if r.ranking_id == 1)
        print(selected_horse_id)
        print(correct_result)

        # horse_numberとhorse_idが違うため、正解でも不正解となってしまう
        if selected_horse_id == correct_result.horse_number:
            answer = '正解です！'
        else:
            answer = f'不正解です。正解は{correct_result.horse.horse_name}です'
        
        next_race = KQT_101.query.get(qid + 1)
        
        return render_template(
            'answer.html',
            answer=answer,
            next_id=qid+1,
            is_last=(next_race is None)
        )
    # ----------------------------------
    # クイズページ
    # ----------------------------------
    return render_template(
        'question.html',
        race_date=race.race_date,
        race_name=race.race_name,
        horse_list=result,
        qid=qid
    )


if __name__ == '__main__':
# --------------------------------------
# 初回のみテーブル作成
# --------------------------------------
    with app.app_context():
        db.create_all()
    app.run(debug=True)