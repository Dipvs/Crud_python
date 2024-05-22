import sqlite3 as sql

con = sql.connect ('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "DATA" TEXT,
    "DESCRICAO" TEXT,
    "TIPO" TEXT
    )'''

cur.execute(sql)
con.commit()
con.close()