# create new database file
# need argument for database name

import sqlite3
import sys

dbpath = sys.argv[1]
conn = sqlite3.connect(dbpath)
conn.close()
