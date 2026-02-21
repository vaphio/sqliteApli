import sqlite3

def open(dbpath):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    return conn, cursor

def close(cursor, conn):
    cursor.close()
    conn.close()
