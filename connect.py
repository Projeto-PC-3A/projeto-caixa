import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="transações"
)
mycursor = mydb.cursor()