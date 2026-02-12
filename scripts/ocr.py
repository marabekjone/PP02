import pytesseract
import cv2
from PIL import Image
import sqlite3
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang="rus+eng")
    return text

def save_to_db(file_path, text):
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO documents (file_path, text, date_added)
    VALUES (?, ?, ?)
    """, (file_path, text, datetime.now()))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    path = input("Введите путь к изображению: ")
    result = recognize_text(path)
    print("\nРаспознанный текст:\n")
    print(result)
    save_to_db(path, result)
    print("\nСохранено в базу данных")
