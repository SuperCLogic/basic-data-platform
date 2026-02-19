import sqlite3

conn = sqlite3.connect("databases/athena.db")
cur = conn.cursor()

cur.execute("SELECT * From user_metrics;")
print(cur.fetchall())

cur.execute("SELECT * From daily_kpis;")
print(cur.fetchall())

conn.close()
