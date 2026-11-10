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

# Update MySQL table

query = "UPDATE STUDENT SET AGE = 23 WHERE Name ='Ram'"
cursorObject.execute(query)
dataBase.commit()

query = "SELECT * FROM STUDENT"
cursorObject.execute(query)
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)

# Delete Data from Table

query = "DELETE FROM STUDENT WHERE NAME = 'Ram'"
cursorObject.execute(query)
dataBase.commit()

query = "SELECT * FROM STUDENT"
cursorObject.execute(query)
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
    
# disconnecting from server
dataBase.close()