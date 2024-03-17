import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SQL.root@1234",
  database="ontology"
)

mycursor = mydb.cursor()

