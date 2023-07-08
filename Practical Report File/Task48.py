#Task 48 - 1/7/23
#Vevan O Narain S7-C

"""The database PHONEBOOK contains a table S7C of structure [name, email, phone]. WAPP 
to input a name and delte the person's details """
import mysql.connector as sql

mydb = sql.connect(host = 'localhost', user = 'root', password = 'the-first-code-ever', database = "PHONEBOOK")
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE PHONEBOOK;")
#mycursor.execute("USE PHONEBOOK;")
#mycursor.execute("CREATE TABLE CONT(NAME VARCHAR(50), EMAIL VARCHAR(100), PHONE INTEGER);")
mycursor.execute("INSERT INTO CONT VALUES('ABC', 'abc@gmail.com', 0123456789)")
mydb.commit();

mycursor.execute("SELECT * FROM CONT")
rows = mycursor.fetchall()
print(rows)

name = input("Enter name to be removed: ")
command = "DELETE FROM CONT WHERE NAME = %s"
value = (name,)

mycursor.execute(command, value)

mycursor.execute("SELECT * FROM CONT")
rows = mycursor.fetchall()
print(rows)