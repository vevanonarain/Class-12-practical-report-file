#Task 47 - 1/7/23
#Vevan O Narain S7-C

"""The database PHONEBOOK contains a table S7C of structure [name, email, phone]. WAPP 
to display all the details"""

import mysql.connector as sql

mydb = sql.connect(host = 'localhost', user = 'root', password = 'the-first-code-ever', database = 'PHONEBOOK')
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE PHONEBOOK;")
#mycursor.execute("USE PHONEBOOK;")
#mycursor.execute("CREATE TABLE CONT(NAME VARCHAR(50), EMAIL VARCHAR(100), PHONE INTEGER);")
#mycursor.execute("INSERT INTO CONT VALUES('Vevan', 'vevanonarain@gmail.com', 98)")
#mydb.commit();
command = "SELECT * FROM CONT"
mycursor.execute(command)
rows = mycursor.fetchall()
print(rows)
