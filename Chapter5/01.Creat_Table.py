# 모듈 추가
import sqlite3

# OPEN DATABASE
conn = sqlite3.connect('./Database/SQL_DDL.db')

# CREATE CURSOR
cur = conn.cursor()

# SQL 명령
CREATE_SQL = """
CREATE TABLE IF NOT EXISTS Item(
    id integer primary key autoincrement ,
    code text not null ,
    name text not null ,
    price integer not null 
)
"""

# SQL 명령 실행
cur.execute(CREATE_SQL)

# DATABASE CLOSE
conn.close()