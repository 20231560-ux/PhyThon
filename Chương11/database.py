import sqlite3
import os

def connect():
    path = os.path.join(os.path.dirname(__file__), "nhansu.db")
    return sqlite3.connect(path)

conn = connect()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nhanvien (
    cccd TEXT PRIMARY KEY,
    hoten TEXT,
    ngaysinh TEXT,
    gioitinh TEXT,
    diachi TEXT
)
""")

conn.commit()
conn.close()

print("✔ Đã tạo bảng nhanvien")