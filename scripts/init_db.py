import sqlite3

conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path TEXT,
    text TEXT,
    date_added TEXT
)
""")

conn.commit()
conn.close()

print("База данных создана")
