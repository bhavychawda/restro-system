
import mysql.connector 
from mysql.connector import Error

passd=input("Enter your database password: ")
# # SERVER CONNECTION

# myserver=mysql.connector.connect(
# host="localhost",
# user="root",
# password=passd,

# )
# CREATE TABLE

# mycursor= myserver.cursor()
# try:
#     mycursor.execute("CREATE DATABASE RESTRO")
#     print("db created successfully")
# except Error as err:
#    print(err)

# DB CONNECTION
mydb=mysql.connector.connect(
host="localhost",
user="root",
password=passd,
database="RESTRO"
)
mydbcursor= mydb.cursor()

# # CREATE TABLES
# # USER TABLE
# # mydbcursor.execute("CREATE TABLE USER(CUSTID INT PRIMARY KEY,NAME VARCHAR(255),PHONE CHAR(10),ADDRESS VARCHAR(255))")
# # #MENU TABLE
# # mydbcursor.execute("CREATE TABLE MENU(ITEM_ID INT PRIMARY KEY,ITEM_NAME VARCHAR(255),PRICE INT )")
# # ORDER TABLE
# mydbcursor.execute("CREATE TABLE ORDERS(ORDER_ID INT PRIMARY KEY,UNIT INT,TOTAL_BILL INT,PAYMENT_MODE VARCHAR(255),ITEM_LIST VARCHAR(255) )")

# ****************************************************************************************************************************************

mydbcursor.execute("ALTER TABLE orders DROP UNIT")
mydbcursor.execute("ALTER TABLE orders MODIFY COLUMN ORDER_ID INT AUTO_INCREMENT")
mydbcursor.execute("ALTER TABLE orders ADD cust_id INT")
mydbcursor.execute("ALTER TABLE orders ADD cust_id INT")