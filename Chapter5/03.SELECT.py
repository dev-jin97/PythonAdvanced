# 모듈 추가
import sqlite3

# OPEN DATABASE
conn = sqlite3.connect('./Database/SQL_DDL.db')

# CREATE CURSOR
cur = conn.cursor()

# SQL 명령
SELECT_SQL = "SELECT * FROM Item LIMIT 2;"

# SQL 명령 실행
cur.execute(SELECT_SQL)

# SELECT : fetchall()
rows = cur.fetchall()
for row in rows:
    print(row)

# DATABASE CLOSE
conn.close()