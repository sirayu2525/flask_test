from models.database import db_session
from models.models import OnegaiContent

# データを作成
c1 = OnegaiContent("お願いします", "5000兆円ください")
c2 = OnegaiContent("助けてください", "ぽんぽんぺいん")
c3 = OnegaiContent("許してください", "なんでもしますから")

# データベースに追加
db_session.add(c1)
db_session.add(c2)
db_session.add(c3)

# コミットして変更を保存
db_session.commit()

print("データを追加しました。")