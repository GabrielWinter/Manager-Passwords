import sqlite3

conn = sqlite3.connect('database.db')

print(conn)

c = conn.cursor()

c.execute("""CREATE TABLE passwords
	(id INTEGER PRIMARY KEY AUTOINCREMENT,
	website TEXT, 
	username TEXT,
	password TEXT)""")


