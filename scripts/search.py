import sqlite3

conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

word = input("Введите слово для поиска: ")

cursor.execute("""
SELECT id, file_path, date_added FROM documents
WHERE text LIKE ?
""", ('%' + word + '%',))

rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]} | Файл: {row[1]} | Дата: {row[2]}")

conn.close()
