#Task 45 - 1/7/23
#Vevan O Narain S7-C

"""Write a python program to create a file user.csv which will contain username and password for some entries"""

import csv

def create_user_csv():
    filename = 'user.csv'
    fieldnames = ['Username', 'Password']

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        while True:
            username = input("Enter username (or 'q' to quit): ")
            if username.lower() == 'q':
                break
            
            password = input("Enter password: ")
            
            writer.writerow({'Username': username, 'Password': password})
            
        print(f"User.csv file has been created with the entered data.")

create_user_csv()