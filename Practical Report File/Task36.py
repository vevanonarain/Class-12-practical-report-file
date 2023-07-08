#Task 36 - 30/6/23
#Vevan O Narain S7-C

"""Write a menu driven program to perform the following operations on a text file “phone.txt”
which contains name and phone number pairs. The menu should have options:
i. Search name and display phone number
ii. Add a new name-phone number pair."""

def search_phone_number():
    name = input("Enter the name to search: ")
    with open("phone.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            pair = line.strip().split(",")
            if pair[0] == name:
                print("Phone number:", pair[1])
                return
        print("Name not found.")

def add_name_phone_number():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    with open("phone.txt", "a") as file:
        file.write(name + "," + phone_number + "\n")
    print("Name and phone number added successfully.")

while True:
    print("\nMenu:")
    print("1. Search name and display phone number")
    print("2. Add a new name-phone number pair")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        search_phone_number()
    elif choice == "2":
        add_name_phone_number()
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")