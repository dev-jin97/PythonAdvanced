# 모듈 추가
import sqlite3

# OPEN DATABASE
conn = sqlite3.connect('./Database/SQL_DDL.db')

# CREATE CURSOR
cur = conn.cursor()

# SQL 명령
INSERT_SQL = "INSERT INTO Item(code, name, price) VALUES (?, ?, ?);"

# SQL 명령 실행
# cur.execute(INSERT_SQL, ('A00001', '게이밍 마우스', 35000))

# 여러개의 데이터 추가
datas = (
    ('A00002', '에어컨 20평형', 350000),
    ('A00003', '최신형 스마트폰', 800000),
    ('A00004', '가성비 노트북', 650000)
)

cur.executemany(INSERT_SQL, datas)

# COMMIT : INSERT, UPDATE, DELETE
conn.commit()

# DATABASE CLOSE
conn.close()