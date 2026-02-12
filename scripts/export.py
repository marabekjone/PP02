import sqlite3

conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

doc_id = input("Введите ID документа: ")

cursor.execute("SELECT text FROM documents WHERE id=?", (doc_id,))
row = cursor.fetchone()

if row:
    with open("export.txt", "w", encoding="utf-8") as f:
        f.write(row[0])
    print("Экспорт выполнен: export.txt")
else:
    print("Документ не найден")

conn.close()
