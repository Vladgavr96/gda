import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE products
(ID
)
""")

conn.commit()
