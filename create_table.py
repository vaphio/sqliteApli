# create table for SQLite database file
# need 2 arguments for database file and table name

import sqlite3
import sys

dbpath = sys.argv[1]
conn = sqlite3.connect(dbpath)

cursor = conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS ''' + sys.argv[2]
sql = sql +  ''' (
     id TEXT PRIMARY KEY,
     book TEXT,
     title TEXT,
     auther TEXT,
     revdt INTEGER
    )'''

cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()
