import sqlite3

dbpath = 'test.db'
conn = sqlite3.connect(dbpath)

cursor = conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS book
    (
     id TEXT PRIMARY KEY,
     yr INTEGER,
     mo INTEGER
    )'''

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
