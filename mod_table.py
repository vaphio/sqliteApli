import sqlite3
import sys

dbpath = 'test.db'
conn = sqlite3.connect(dbpath)

cursor = conn.cursor()
sql = '''ALTER TABLE book RENAME TO ''' + sys.argv[1]

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
