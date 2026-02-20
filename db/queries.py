import sqlite3


DB_PATH = "shop.db"

def add_item(text):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (title) VALUES (?)", (text,))
        conn.commit()

def get_items(filter_type="all"):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if filter_type == "bought":
            cursor.execute("SELECT * FROM items WHERE status = 1")
        elif filter_type == "unbought":
            cursor.execute("SELECT * FROM items WHERE status = 0")
        else:
            cursor.execute("SELECT * FROM items")
        return cursor.fetchall()
