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

# show the result of decribe sentence
cursorObject.execute("DESCRIBE STUDENT")

myresult = cursorObject.fetchall()
print(myresult)

# disconnecting from server
dataBase.close()

'''
Try describe table
'''