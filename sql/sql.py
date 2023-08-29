import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
product TEXT,
shop TEXT,
price int
)
""")

'''cursor.execute('INSERT INTO products(product, shop, price) values("Яблоки", "Дикси", 100)')
cursor.execute("INSERT INTO products(product,shop,price) Values('бананы', 'Дикси', 50)")
cursor.execute("INSERT INTO products(product,shop,price) Values('кросовки', 'спортмастер', 2000)")
cursor.execute("INSERT INTO products(product,shop,price) Values('отвертка', 'домовой', 300)")
cursor.execute("INSERT INTO products(product,shop,price) Values('спортивная куртка', 'спортмастер', 3000)")
cursor.execute("INSERT INTO products(product,shop,price) Values('спортивные штаны', 'спортмастер', 3000)")'''

'''cursor.execute('SELECT product FROM products')  # * чтобы запросить все поля
res = cursor.fetchall()
for i in res:
    print(i)
'''

'''cursor.execute('SELECT * FROM products WHERE price<1000')
res = cursor.fetchall()
for i in res:
    print(i)'''

'''cursor.execute('SELECT * FROM products WHERE price<1000 AND shop="Дикси"') # Для оператора или используйте OR
res = cursor.fetchall()
for i in res:
    print(i)'''


'''cursor.execute('SELECT product FROM products WHERE price>1000')
res = cursor.fetchall()
for i in res:
    print(i)'''

'''cursor.execute('SELECT DISTINCT shop FROM products') #получение уникальных названий магазинов
res = cursor.fetchall()
for i in res:
    print(i)'''

'''cursor.execute('SELECT count(DISTINCT shop) FROM products')
res = cursor.fetchall()
for i in res:
    print(i)'''

'''cursor.execute('SELECT MIN(price) FROM products')
res = cursor.fetchall()
for i in res:
    print(i)

cursor.execute('SELECT MAX(price) FROM products')
res = cursor.fetchall()
for i in res:
    print(i)

cursor.execute('SELECT AVG(price) FROM products')
res = cursor.fetchall()
for i in res:
    print(i)'''

'''cursor.execute("""CREATE TABLE if not exists shops
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  shop_name text,
                  address text)
             """)
cursor.execute("INSERT INTO shops(shop_name,address) Values('Дикси', 'Улица Пушкина д.7')")
cursor.execute("INSERT INTO shops(shop_name,address) Values('спортмастер', 'Улица Ленина д.11')")
cursor.execute("INSERT INTO shops(shop_name,address) Values('домовой', 'Улица Бакунина д.3')")'''

#cursor.execute("INSERT INTO products(product,shop,price) Values('кофе', 'Пятерочка', 500)")

cursor.execute('SELECT product, address FROM products LEFT JOIN shops ON products.shop = shops.shop_name')
res = cursor.fetchall()
for i in res:
    print(i)



conn.commit()
