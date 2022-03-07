import sqlite3
con=sqlite3.connect("olympic.db")
cur=con.cursor()
print(cur.execute("SELECT * FROM tokyo2020").fetchall())
