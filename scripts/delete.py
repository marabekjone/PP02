import sqlite3

conn = sqlite3.connect("documents.db")
cursor = conn.cursor()

doc_id = input("Введите ID документа для удаления: ")

cursor.execute("DELETE FROM documents WHERE id=?", (doc_id,))
conn.commit()

print("Документ удалён")
conn.close()
