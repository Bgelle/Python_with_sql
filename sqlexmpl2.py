# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE DATABASE mydatabase")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
database="mydatabase"
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")


# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)