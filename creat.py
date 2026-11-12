# import sqlite3
# con = sqlite3.connect("database.db")
# corsor = con.cursor()
# corsor.execute("""
#     CREATE TABLE IF NOT EXISTS user(
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       Ism TEXT NOT NULL,
#       Familiya TEXT NOT NULL,
#       Yosh INTEGER)""")
# con.commit()
# con.close()
# print("Data baza yaratildi")

# import sqlite3
# con = sqlite3.connect("database.db")
# corsor = con.cursor()
# corsor.execute("""
#         INSERT INTO user(Ism,Familiya,Yosh)
#         VALUES (?,?,?)""",("Mark","Jones",30))
# con.commit()
# con.close()
# print("Malumot qoshildi")




# import sqlite3
# con = sqlite3.connect("database.db")
# corsor = con.cursor()
# corsor.execute("""SELECT * FROM user WHERE id = 2;""")
# print(corsor.fetchone())
# con.commit()
# con.close()

# import sqlite3
# con = sqlite3.connect("database.db")
# corsor = con.cursor()
# corsor.execute("""
#         INSERT INTO user(Ism,Familiya,Yosh)
#         VALUES (?,?,?)""",("Mark","Jones",30))
# con.commit()
# con.close()
# print("Malumot qoshildi")

# import sqlite3

# con = sqlite3.connect("talabalar.db")
# cursor = con.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS talabalar(
#     id SERIAL PRIMARY KEY,
#     ism VARCHAR(50),
#     familiya VARCHAR(50),
#     yosh INTEGER,
#     guruh VARCHAR(20),
#     bahosi NUMERIC(4,2)
# )
# """)

# talabalar = [
#     ("Ali", "Valiyev", 20, "101-guruh", 5),
#     ("Vali", "Karimov", 19, "102-guruh", 4),
#     ("Madina", "Aliyeva", 21, "101-guruh", 5),
#     ("Aziza", "Toshpulatova", 18, "103-guruh", 4),
#     ("Sardor", "Ergashev", 20, "102-guruh", 3),
# ]

# cursor.executemany("""
# INSERT INTO talabalar
# (ism,familiya,yosh,guruh,bahosi)
# VALUES (?,?,?,?,?)
# """, talabalar )

# con.commit()
# con.close()

# print("Ma'lumotlar qo'shildi")


# import psycopg2
# from psycopg2 import Error

# connection = None
# cursor = None

# try:
#     connection = psycopg2.connect(
#         user="postgres",
#         password="7654",
#         host="127.0.0.1",
#         port="5432",
#         database="carshop"
#     )

#     cursor = connection.cursor()

#     print(connection.get_dsn_parameters())

#     cursor.execute("SELECT version();")
#     record = cursor.fetchone()

#     print("PostgreSQL version:", record[0])

# except (Exception, Error) as error:
#     print("Error connecting to PostgreSQL:", error)

# finally:
#     if cursor is not None:
#         cursor.close()

#     if connection is not None:
#         connection.close()
#         print("PostgreSQL connection closed.")

# import psycopg2
# from psycopg2 import Error
# try :
#     connection = psycopg2.connect(user="postgres",
#                                   password="7654",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="carshop")
#     cursor = connection.cursor()
#     create_table_query = '''CREATE TABLE car
#           (ID INT PRIMARY KEY    NOT NULL,
#           MODEL           TEXT   NOT NULL,
#           PRICE         REAL,
#           YEAR          TEXT     NOT NULL,
#           COMPANY       TEXT     NOT NULL);'''
#     cursor.execute(create_table_query)
#     connection.commit()
#     print("Table created successfully in PostgreSQL ")

# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")

import psycopg2
from psycopg2 import Error

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        user="postgres",
        password="xudashukur10",
        host="127.0.0.1",
        port="5432",
        database="carshop"
    )
    cursor = connection.cursor()
    yaratish = "INSERT INTO cars (id,model,price)VALUES (%s,%s,%s) "
    qoshish = ("DOGE CHARGER",55000)
    cursor.execute(yaratish,qoshish)
    connection.commit()
    print("malumot qoshildi")
    
    
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
        print("PostgreSQL connection is closed")






































































