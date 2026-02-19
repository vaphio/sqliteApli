import sqlite3
import sys

dbpath = 'book.db'

def open(dbpath):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    return conn, cursor

def close(cursor, conn):
    cursor.close()
    conn.close()

def prinfo(info):
    for line in info:
        print(line)

conn, cursor = open(dbpath)
sql = '''PRAGMA TABLE_INFO(''' + sys.argv[1] + ')'
print(sql)
db_info = cursor.execute(sql).fetchall()
prinfo(db_info)

close(cursor, conn)
