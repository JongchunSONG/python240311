# 제품데이터 입출력.py

import sqlite3

class ProductManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                price REAL
                                )''')
        self.conn.commit()

    def insert_product(self, id, name, price):
        self.cursor.execute("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", (id, name, price))
        self.conn.commit()
        print("Product inserted successfully.")

    def update_product(self, id, name, price):
        self.cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (name, price, id))
        self.conn.commit()
        print("Product updated successfully.")

    def delete_product(self, id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        self.conn.commit()
        print("Product deleted successfully.")

    def select_product(self, id):
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (id,))
        product = self.cursor.fetchone()
        if product:
            print("Product ID:", product[0])
            print("Product Name:", product[1])
            print("Product Price:", product[2])
        else:
            print("Product not found.")

# 샘플 데이터 준비
sample_data = [
    (1, "Laptop", 1500.0),
    (2, "Smartphone", 800.0),
    (3, "Tablet", 400.0),
    (4, "Headphones", 100.0),
    (5, "Smartwatch", 300.0),
    (6, "Monitor", 300.0),
    (7, "Keyboard", 50.0),
    (8, "Mouse", 20.0),
    (9, "Printer", 200.0),
    (10, "Scanner", 150.0)
]

# 데이터베이스 생성 및 관리자 객체 생성
product_manager = ProductManager("products.db")

# 샘플 데이터 추가
for data in sample_data:
    product_manager.insert_product(*data)

# 샘플 데이터 조회
print("\nSample Data:")
for i in range(1, 11):
    product_manager.select_product(i)

# 제품 업데이트
product_manager.update_product(10, "New Scanner Model", 180.0)

# 업데이트된 제품 조회
print("\nUpdated Product:")
product_manager.select_product(10)

# 제품 삭제
product_manager.delete_product(8)

# 삭제된 제품 조회
print("\nDeleted Product:")
product_manager.select_product(8)

# 데이터베이스 연결 종료
product_manager.conn.close()
