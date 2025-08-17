import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # الاتصال بسيرفر MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",             # غيّرها لاسم المستخدم بتاعك
            password="your_password" # غيّرها للباسورد بتاعك
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:   # ✅ هنا بنعمل handling للـ mysql.connector.Error
        print(f"MySQL Error: {e}")

    except Exception as e:  # ✅ للتأكد لو في خطأ عام تاني غير MySQL
        print(f"General Error: {e}")

    finally:
        if connection and
