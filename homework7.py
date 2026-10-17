
import sqlite3


# Подключение к базе данных
connect = sqlite3.connect("store.db")
cursor = connect.cursor()


# Создание таблицы
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
""")

connect.commit()


# CREATE — добавление товара
def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    connect.commit()
    print("Товар добавлен!")


# READ — получение всех товаров
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    for product in products:
        print(product)


# UPDATE — изменение цены товара
def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    connect.commit()

    if cursor.rowcount > 0:
        print("Цена товара обновлена!")
    else:
        print("Товар не найден!")


# DELETE — удаление товара
def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    connect.commit()

    if cursor.rowcount > 0:
        print("Товар удалён!")
    else:
        print("Товар не найден!")


# Проверка работы программы
create_product("Футболка", 1850, 20)
create_product("Худи", 3500, 10)

print("\nСписок товаров:")
read_products()

update_product(1, 2000)

print("\nПосле изменения цены:")
read_products()

delete_product(2)

print("\nПосле удаления товара:")
read_products()

# Закрытие соединения с базой данных
connect.close()
