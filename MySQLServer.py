# MySQLServer.py
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       # غيّرها لو عندك يوزر مختلف
        password="password" # غيّرها بالباسورد بتاعك
    )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
