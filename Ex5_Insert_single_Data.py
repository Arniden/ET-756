# importing required libraries
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="",
  passwd =""
  database = ""
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = ("Ram", "CSE", "85", "B", "19")

   
cursorObject.execute(sql, val)

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION)\
VALUES (%s, %s, %s, %s)"
val = ("Jack", "CSE", "85", "B")
cursorObject.execute(sql, val)

dataBase.commit()

# disconnecting from server
dataBase.close()

'''
Name, age, id, major
Sam, 18, 123, CS
Tom, 20, 456, ET
'''