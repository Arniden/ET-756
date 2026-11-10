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

# Select data from MySQL table using Python

query = "SELECT NAME, ROLL FROM STUDENT"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
#exit()
# Where clause

query = "SELECT * FROM STUDENT where AGE >=20"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)

# Order By clause

query = "SELECT * FROM STUDENT ORDER BY NAME DESC"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)

# Limit Clause

query = "SELECT * FROM STUDENT LIMIT 2 OFFSET 1"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()

'''
Extract student with CS major
'''