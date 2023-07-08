#Task 49 - 1/7/23
#Vevan O Narain S7-C

"""Write a menu based program to insert, remove and display items from a table S7C in database SCHOOL. The 
structure of the database is [id, name, phone no.]"""

import mysql.connector as sql

mydb = sql.connect(host = 'localhost', user = 'root', password = 'the-first-code-ever', database = "SCHOOL")
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE S7C(ID CHAR(6), NAME VARCHAR(50), PHONE INTEGER);")

def TABLE_APPEND(id, name, phone):
    command = ("INSERT INTO S7C (id, name, phone) VALUES (%s, %s, %s)")
    values = (id, name, phone)
    mycursor.execute(command, values)
    mydb.commit()

def TABLE_REMOVE(name):
    command = "DELETE FROM S7C WHERE NAME = %s"
    value = (name,)
    mycursor.execute(command, value)
    mydb.commit()

def TABLE_DISPLAY():
    command = "SELECT * FROM S7C"
    mycursor.execute(command)

    items = mycursor.fetchall()
    if not items:
        print("No items found.")
    else:
        for item in items:
            print("ID:", item[0])
            print("Name:", item[1])
            print("Phone No.:", item[2])
            print()

while True:
    print("Operations on database table:\n1.Append\n2.Remove\n3.Display\n4.Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        student_id = input("Enter Student id: ")
        name = input("Enter Name: ")
        phone = int(input("Enter phone number: "))
        TABLE_APPEND(student_id, name, phone)
    elif choice == "2":
        name = input("Enter name to be removed: ")
        TABLE_REMOVE(name)
    elif choice == "3":
        TABLE_DISPLAY()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid Choice")