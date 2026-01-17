from app import app
from datetime import date
from models import db,KQT_101, KQT_201, KQT_301

with app.app_context():
    # --------------------------------------
    # レース名登録
    # --------------------------------------
    race = KQT_101(
        race_date = date(2025, 12, 28), #date型に変換(2024−12−24)して格納
        race_name = '有馬記念'
    )
    db.session.add(race)
    db.session.commit()

    # --------------------------------------
    # 馬名登録
    # --------------------------------------
    horse1 = KQT_201(horse_name='エキサイトバイオ')
    horse2 = KQT_201(horse_name='シンエンペラー')
    horse3 = KQT_201(horse_name='ジャスティンパレス')
    horse4 = KQT_201(horse_name='ミュージアムマイル')
    horse5 = KQT_201(horse_name='レガレイラ')
    horse6 = KQT_201(horse_name='メイショウタバル')
    horse7 = KQT_201(horse_name='サンライズジパング')
    horse8 = KQT_201(horse_name='シュヴァリエローズ')
    horse9 = KQT_201(horse_name='ダノンデサイル')
    horse10 = KQT_201(horse_name='コスモキュランダ')
    horse11 = KQT_201(horse_name='ミステリーウェイ')
    horse12 = KQT_201(horse_name='マイネルエンペラー')
    horse13 = KQT_201(horse_name='アドマイヤテラ')
    horse14 = KQT_201(horse_name='アラタ')
    horse15 = KQT_201(horse_name='エルトンバローズ')
    horse16 = KQT_201(horse_name='タスティエーラ')

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
        ranking_id=8
    )
    result2 = KQT_301(
        race_id=race.race_id,
        horse_id=horse2.horse_id,
        waku_number=1,
        horse_number=2,
        ranking_id=14
    )
    result3 = KQT_301(
        race_id=race.race_id,
        horse_id=horse3.horse_id,
        waku_number=2,
        horse_number=3,
        ranking_id=7
    )
    result4 = KQT_301(
        race_id=race.race_id,
        horse_id=horse4.horse_id,
        waku_number=2,
        horse_number=4,
        ranking_id=1
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
        ranking_id=13
    )
    result7 = KQT_301(
        race_id=race.race_id,
        horse_id=horse7.horse_id,
        waku_number=4,    
        horse_number=7,
        ranking_id=5
    )
    result8 = KQT_301(
        race_id=race.race_id,
        horse_id=horse8.horse_id,
        waku_number=4,
        horse_number=8,
        ranking_id=10
    )
    result9 = KQT_301(
        race_id=race.race_id,
        horse_id=horse9.horse_id,
        waku_number=5,
        horse_number=9,
        ranking_id=3
    )
    result10 = KQT_301(
        race_id=race.race_id,
        horse_id=horse10.horse_id,
        waku_number=5,
        horse_number=10,
        ranking_id=2
    )
    result11 = KQT_301(
        race_id=race.race_id,
        horse_id=horse11.horse_id,
        waku_number=6,
        horse_number=11,
        ranking_id=16
    )
    result12 = KQT_301(
        race_id=race.race_id,
        horse_id=horse12.horse_id,
        waku_number=6,
        horse_number=12,
        ranking_id=9
    )
    result13 = KQT_301(
        race_id=race.race_id,
        horse_id=horse13.horse_id,
        waku_number=7,
        horse_number=13,
        ranking_id=11
    )
    result14 = KQT_301(
        race_id=race.race_id,
        horse_id=horse14.horse_id,
        waku_number=7,
        horse_number=14,
        ranking_id=15
    )
    result15 = KQT_301(
        race_id=race.race_id,
        horse_id=horse15.horse_id,
        waku_number=8,
        horse_number=15,
        ranking_id=12
    )
    result16 = KQT_301(
        race_id=race.race_id,
        horse_id=horse16.horse_id,
        waku_number=8,
        horse_number=16,
        ranking_id=6
    )
    
    db.session.add_all([result1,result2,result3,result4,result5,result6,result7,result8,result9,result10,result11,result12,result13,result14,result15,result16])
    db.session.commit()

    print('データ登録完了')
