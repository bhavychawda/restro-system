import mysql.connector 
from mysql.connector import Error

# passd=input("Enter your database password: ")


mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Qwerty#@123",
database="RESTRO"
)
mydbcursor= mydb.cursor()




#Place order function
def place_order(total_bill,pay_mode,item_list):
    
    sql = "INSERT INTO orders (TOTAL_BILL,PAYMENT_MODE,ITEM_LIST) VALUES(%s,%s,%s)"
    val = (total_bill,pay_mode,item_list)
    mydbcursor.execute(sql,val)
    mydb.commit()

