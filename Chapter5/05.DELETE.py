# 모듈 추가
import sqlite3

# OPEN DATABASE
conn = sqlite3.connect('./Database/SQL_DDL.db')

# CREATE CURSOR
cur = conn.cursor()

# SQL 명령
DELETE_SQL = "DELETE FROM Item WHERE code = 'A00002';"

# SQL 명령 실행
cur.execute(DELETE_SQL)

# COMMIT
conn.commit()

# DATABASE CLOSE
conn.close()