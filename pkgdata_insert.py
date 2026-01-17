from app import app
from datetime import date
from models import db,KQT_101, KQT_201, KQT_301

with app.app_context():
    # --------------------------------------
    # レース名登録
    # --------------------------------------
    race = KQT_101(
        race_date = date(2024, 12, 24), #date型に変換(2024−12−24)して格納
        race_name = '有馬記念'
    )
    db.session.add(race)
    db.session.commit()

    # --------------------------------------
    # 馬名登録
    # --------------------------------------
    horse1 = KQT_201(horse_name='ダノンデサイル')
    horse2 = KQT_201(horse_name='ドウデュース')
    horse3 = KQT_201(horse_name='アーバンシック')
    horse4 = KQT_201(horse_name='ブローンザホーン')
    horse5 = KQT_201(horse_name='ベラジオオペラ')
    horse6 = KQT_201(horse_name='ローシャムパーク')
    horse7 = KQT_201(horse_name='スターズオンアース')
    horse8 = KQT_201(horse_name='レガレイラ')
    horse9 = KQT_201(horse_name='ディープボンド')
    horse10 = KQT_201(horse_name='プログノーシス')
    horse11 = KQT_201(horse_name='ジャスティンパレス')
    horse12 = KQT_201(horse_name='シュトルーヴェ')
    horse13 = KQT_201(horse_name='スタニングローズ')
    horse14 = KQT_201(horse_name='ダノンベルーガ')
    horse15 = KQT_201(horse_name='ハヤヤッコ')
    horse16 = KQT_201(horse_name='シャフリヤール')

    db.session.add_all([horse1,horse2,horse3,horse4,horse5,horse6,horse7,horse8,horse9,horse10,horse11,horse12,horse13,horse14,horse15,horse16])
    db.session.commit()

    # --------------------------------------
    # レース結果登録
    # --------------------------------------
    result1 = KQT_301(
        race_id=race.race_id,
        horse_id=horse1.horse_id,
        waku_number=1,
        horse_number=1,
        ranking_id=3
    )
    result2 = KQT_301(
        race_id=race.race_id,
        horse_id=horse2.horse_id,
        waku_number=1,
        horse_number=2,
        ranking_id=16
    )
    result3 = KQT_301(
        race_id=race.race_id,
        horse_id=horse3.horse_id,
        waku_number=2,
        horse_number=3,
        ranking_id=6
    )
    result4 = KQT_301(
        race_id=race.race_id,
        horse_id=horse4.horse_id,
        waku_number=2,
        horse_number=4,
        ranking_id=12
    )
    result5 = KQT_301(
        race_id=race.race_id,
        horse_id=horse5.horse_id,
        waku_number=3,
        horse_number=5,
        ranking_id=4
    )
    result6 = KQT_301(
        race_id=race.race_id,
        horse_id=horse6.horse_id,
        waku_number=3,
        horse_number=6,
        ranking_id=7
    )
    result7 = KQT_301(
        race_id=race.race_id,
        horse_id=horse7.horse_id,
        waku_number=4,    
        horse_number=7,
        ranking_id=14
    )
    result8 = KQT_301(
        race_id=race.race_id,
        horse_id=horse8.horse_id,
        waku_number=4,
        horse_number=8,
        ranking_id=1
    )
    result9 = KQT_301(
        race_id=race.race_id,
        horse_id=horse9.horse_id,
        waku_number=5,
        horse_number=9,
        ranking_id=13
    )
    result10 = KQT_301(
        race_id=race.race_id,
        horse_id=horse10.horse_id,
        waku_number=5,
        horse_number=10,
        ranking_id=11
    )
    result11 = KQT_301(
        race_id=race.race_id,
        horse_id=horse11.horse_id,
        waku_number=6,
        horse_number=11,
        ranking_id=5
    )
    result12 = KQT_301(
        race_id=race.race_id,
        horse_id=horse12.horse_id,
        waku_number=6,
        horse_number=12,
        ranking_id=10
    )
    result13 = KQT_301(
        race_id=race.race_id,
        horse_id=horse13.horse_id,
        waku_number=7,
        horse_number=13,
        ranking_id=8
    )
    result14 = KQT_301(
        race_id=race.race_id,
        horse_id=horse14.horse_id,
        waku_number=7,
        horse_number=14,
        ranking_id=9
    )
    result15 = KQT_301(
        race_id=race.race_id,
        horse_id=horse15.horse_id,
        waku_number=8,
        horse_number=15,
        ranking_id=15
    )
    result16 = KQT_301(
        race_id=race.race_id,
        horse_id=horse16.horse_id,
        waku_number=8,
        horse_number=16,
        ranking_id=2
    )
    
    db.session.add_all([result1,result2,result3,result4,result5,result6,result7,result8,result9,result10,result11,result12,result13,result14,result15,result16])
    db.session.commit()

    print('データ登録完了')
