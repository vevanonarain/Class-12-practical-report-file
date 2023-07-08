#Task 41 - 1/7/23
#Vevan O Narain S7-C

"""Write a menu driven python program to insert, search, update and display records
in a binary file"""

import pickle
import os

while True:
    print("Operations on a binary file:\n1.Insert a record\n2. Search a record\n3. Update a record\n4. Display a record\n5. Delete a record\n6. Exit")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        insert_rec()

    elif ch == 2:
        search_rec()

    elif ch == 3:
        update_rec()

    elif ch == 4:
        display_rec()

    elif ch == 5:
        delete_rec()

    elif ch == 6:
        print("Exiting program....")
        break

    else:
        print("Invalid Choice.")

def insert_rec():
    f = open("sales.dat","ab")
    c = 'yes'

    while True:
        sales_id = int(input("Enter ID:"))
        name = input("Enter Name:")
        city = input("Enter City:")

        d = {"SalesId":sales_id,"Name":name,"City":city}
        pickle.dump(d,f)
        
        print("Record Inserted.")
        print("Want to insert more records, Type yes:")
        
        c = input()
        c = c.lower()
        if c not in 'yes':
            break
    
    f.close()
    
def display_rec():
    f = open("sales.dat","rb")
    
    try:
        while True:
            d = pickle.load(f)
            print(d)
    except:
       f.close()

def search_rec():
    f = open("sales.dat","rb")
    s=int(input("Enter id to search:"))
    f1 = 0

    try:
        while True:
            d = pickle.load(f)
            if d["SalesId"] == s:
                f1=1
                print(d)
                break
    except:
        f.close()

    if f1 == 0:
        print("Record not found...")
    else:
        print("Record found...")

def update_rec():
    f1 = open("sales.dat","rb")
    f2 = open("temp.dat","wb")
    s = int(input("Enter id to update:"))

    try:
        while True:
            d = pickle.load(f1)

            if d["SalesId"]==s:
                d["Name"]=input("Enter Name:")
                d["City"]=input("Enter City:")

            pickle.dump(d,f2)

    except:
        print("Record Updated.")

    f1.close()
    f2.close()
    os.remove("sales.dat")
    os.rename("temp.dat","sales.dat")

def delete_rec():
    f1 = open("sales.dat","rb")
    f2 = open("temp.dat","wb")
    s = int(input("Enter id to delete:"))

    try:
        while True:
            d = pickle.load(f1)
            if d["SalesId"] != s:
                pickle.dump(d,f2)

    except EOFError:
        print("Record Deleted.")

    f1.close()
    f2.close()
    os.remove("sales.dat")
    os.rename("temp.dat","sales.dat")