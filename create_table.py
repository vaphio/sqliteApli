# create table for SQLite database file
# need 2 arguments for database file and table name

import sqlite3

dbpath = sys.argv[1]
conn = sqlite3.connect(dbpath)

cursor = conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS''' + sys.argv[2] +
    ''' (
     id TEXT PRIMARY KEY,
     name TEXT,
     auther TEXT,
     revdt INTEGER
    )'''

cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()
