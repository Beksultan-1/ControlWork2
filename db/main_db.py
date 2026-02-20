import sqlite3

# 1. Создание базы и таблицы
def init_db():
    with sqlite3.connect("shop.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                status INTEGER DEFAULT 0
            )
        """)
        conn.commit()

# 2. Добавление товара
def add_item(text):
    with sqlite3.connect("shop.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (title) VALUES (?)", (text,))
        conn.commit()

# 3. Получение списка (с учетом фильтров)
def get_items(filter_type="all"):
    with sqlite3.connect("shop.db") as conn:
        cursor = conn.cursor()
        if filter_type == "bought":
            cursor.execute("SELECT * FROM items WHERE status = 1")
        elif filter_type == "unbought":
            cursor.execute("SELECT * FROM items WHERE status = 0")
        else:
            cursor.execute("SELECT * FROM items")
        return cursor.fetchall()

# 4. Обновление статуса (нужно для работы галочек)
def toggle_item(item_id, val):
    with sqlite3.connect("shop.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE items SET status = ? WHERE id = ?", (int(val), item_id))
        conn.commit()

# Это позволит запустить init_db() автоматически при старте
if __name__ == "__main__":
    init_db()
