import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE products
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
product TEXT,
shop TEXT,
price int
)
""")

conn.commit()
