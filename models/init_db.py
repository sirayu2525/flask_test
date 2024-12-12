import sys
print(sys.path)  # Pythonのインポートパスを出力


from models.database import init_db

if __name__ == '__main__':
    init_db()
    print("データベースを初期化しました。")
