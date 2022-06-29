import mysql.connector
import os

sqlPass = os.getenv('SQLPASS')
from mysql.connector import errorcode

try:
  mydb = mysql.connector.connect()
  my_cursor = mydb.cursor()

  # my_cursor.execute("CREATE DATABASE stockdata")

  my_cursor.execute("SHOW DATABASES")
  for db in my_cursor:
      print(db)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password", err)
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  mydb.close()