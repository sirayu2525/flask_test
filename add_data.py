from models.database import db_session
from models.models import OnegaiContent, User
from sqlalchemy.exc import IntegrityError

# データを作成
c1 = OnegaiContent("お願いします", "5000兆円ください")
c2 = OnegaiContent("助けてください", "ぽんぽんぺいん")

d1 = User("user1", "password1")

# データベースに追加
try:
    db_session.add(c1)
    db_session.add(c2)
    db_session.add(d1)
    # コミットして変更を保存
    db_session.commit()
    print("データを追加しました。")
except IntegrityError as e:
    db_session.rollback()
    print("データの追加に失敗しました。重複するデータが存在します。")
    print(e)