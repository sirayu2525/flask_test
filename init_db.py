import sys
import os

# プロジェクトのルートディレクトリをインポートパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.database import init_db

if __name__ == '__main__':
    init_db()
    print("データベースを初期化しました。")
