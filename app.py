from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# --------------------------------------
# 問題リストの用意
# --------------------------------------
quiz_list = [
    {
        'race_year':2023,
        'race_name':'有馬記念',
        'horse_list':['イクイノックス','ジェラルディーナ','エフフォーリア'],
        'answer':'イクイノックス'
    },
    {
        'race_year':2021,
        'race_name':'皐月賞',
        'horse_list':['ステラヴェローチェ','タイトルホルダー','エフフォーリア'],
        'answer':'エフフォーリア'
    },
    {
        'race_year':2018,
        'race_name':'マイルCS',
        'horse_list':['エアスピネル','ステルヴィオ','ペルシアンナイト'],
        'answer':'ステルヴィオ'
    },
    {
        'race_year':2019,
        'race_name':'スプリンターズS',
        'horse_list':['タワーオブロンドン','ダノンスマッシュ','モズスーパーフレア'],
        'answer':'タワーオブロンドン'
    },
    {
        'race_year':2024,
        'race_name':'秋華賞',
        'horse_list':['チェルヴィニア','ボンドガール','ステレンボッシュ'],
        'answer':'チェルヴィニア'
    }
]

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
    if qid < 1 or qid > len(quiz_list):
        return '終了しました！'
    
    quiz = quiz_list[qid -1]
    # ----------------------------------
    # 正解確認ページ
    # ----------------------------------
    if request.method == 'POST':
        selected = request.form.get('selected_horse') # htmlのname要素selected_horseのvalue要素を取得
        correct = quiz['answer']

        if selected == correct:
            result = '正解です！'
        else:
            result = f'不正解です。正解は{correct}です'
        
        return render_template(
            'answer.html',
            answer=result,
            next_id=qid+1,
            is_last=(qid == len(quiz_list))
        )
    # ----------------------------------
    # クイズページ
    # ----------------------------------
    return render_template(
        'question.html',
        race_year=quiz['race_year'],
        race_name=quiz['race_name'],
        horse_list=quiz['horse_list'],
        qid=qid
    )


if __name__ == '__main__':
    app.run(debug=True)