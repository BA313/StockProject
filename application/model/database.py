import mysql.connector
from mysql.connector import errorcode
from decouple import config

def connectToDB():
  #get password from .env file
  sqlPass = config('SQLPASS')

  #make sure passwords do not use special characters
  try:
    mydb = mysql.connector.connect(
      host='localhost',
      user='root',
      password=str(sqlPass))
    return mydb

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password", err)
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    mydb.close()

def closeDB(db):
  db.close()

#mydb.cursor()
def showDatabases(my_cursor):
  # my_cursor.execute("CREATE DATABASE stockdata")
  # cursors can execute sql commands
  my_cursor.execute("SHOW DATABASES")
  for db in my_cursor:
    print(db)