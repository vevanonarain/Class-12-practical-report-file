#Task 44 - 1/7/23
#Vevan O Narain S7-C

"""Define the following functions and write a menu based program to execute those functions:
1) email.csv is a CSV file, having names and email_id of various persons persons stored 
   in it. Define a python function CSV_append to create/append more records.
2) email.csv is a CSV file, having names and email_id of various persons stored in it. Define
   a python function CSV_search to read, search and return the email_id for a given name. If 
   the given name is not found, NULL value should be returned.
3) email.csv is a CSV file, having names and email_id of various persons stored in it. Define 
   a python function CSV_count to read, check, count and display the details of all the persons
   having email_id ending with @india.in"""

def CSV_append():
    f = open("email.csv", "a")

    name = input("Enter name: ")
    email = input("Enter email: ")

    l = [name, email]

    w = csv.writer(f)
    w.writerows(l)

def CSV_search():
    f = open("email.csv", "r")
    search = input("Enter name you want to search: ")

    r = csv.reader(f)

    for i in r:
        if i[0] == search:
            print(i[0])
            print(i[1])
        else:
            print("NULL")

def CSV_count():
    f = open("email.csv", "r")
    r = csv.reader(f)

    sum = 0

    for i in r:
        x = i[1].split('@')
        if x[1].lower() == 'india.in':
            sum += 1

    return sum

while True:
    print("Operations on CSV files:\n1.Append\n2.Search\n3.Count\n4.Quit\n")
    choice = input("Enter Choice Number: ")

    if choice == "1":
        CSV_append()
    elif choice == "2":
        CSV_search()
    elif choice == "3":
        CSV_count()
    elif choice == "4":
        print("Exiting....")
        break
    else:
        print("Invalid Argument")