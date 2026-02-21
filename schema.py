# display table schema
# need 2 arguments for dbfile and table name

import sqfunc
import sys

def prinfo(info):
    for line in info:
        print(line)

if len(sys.argv)<3:
    print('nees 2 arguments for database file name and table name')
    exit
else:
    dbpath = sys.argv[1]
    conn, cursor = sqfunc.open(dbpath)
    sql = '''PRAGMA TABLE_INFO(''' + sys.argv[2] + ')'
    print(sql)
    db_info = cursor.execute(sql).fetchall()
    prinfo(db_info)

    sqfunc.close(cursor, conn)
