import sqlite3

dbpath = 'test.db'
conn = sqlite3.connect(dbpath)
conn.close()
