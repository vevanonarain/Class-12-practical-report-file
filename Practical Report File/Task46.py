#Task 46 - 1/7/23
#Vevan O Narain S7-C

"""Write a menu based python program for csv file donor.csv to append, display, search, modify, 
delete items from the csv file."""

import csv

def read_csv_file(filename):
    rows = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rows.append(row)
    return rows

def write_csv_file(filename, rows):
    fieldnames = rows[0].keys()
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def display_donors(donors):
    if len(donors) == 0:
        print("No donors found.")
    else:
        for donor in donors:
            print(f"Name: {donor['Name']}, Blood Group: {donor['Blood Group']}, Phone Number: {donor['Phone Number']}")

def search_donor(donors, search_name):
    matching_donors = []
    for donor in donors:
        if donor['Name'].lower() == search_name.lower():
            matching_donors.append(donor)
    return matching_donors

def append_donor(donors):
    name = input("Enter donor name: ")
    blood_group = input("Enter blood group: ")
    phone_number = input("Enter phone number: ")
    donor = {'Name': name, 'Blood Group': blood_group, 'Phone Number': phone_number}
    donors.append(donor)
    print("Donor added successfully.")

def modify_donor(donors):
    search_name = input("Enter the donor name to modify: ")
    matching_donors = search_donor(donors, search_name)
    if len(matching_donors) == 0:
        print("Donor not found.")
    else:
        print("Matching donors:")
        display_donors(matching_donors)
        new_name = input("Enter new name: ")
        new_blood_group = input("Enter new blood group: ")
        new_phone_number = input("Enter new phone number: ")
        for donor in matching_donors:
            donor['Name'] = new_name
            donor['Blood Group'] = new_blood_group
            donor['Phone Number'] = new_phone_number
        print("Donor details modified successfully.")

def delete_donor(donors):
    search_name = input("Enter the donor name to delete: ")
    matching_donors = search_donor(donors, search_name)
    if len(matching_donors) == 0:
        print("Donor not found.")
    else:
        print("Matching donors:")
        display_donors(matching_donors)
        choice = input("Are you sure you want to delete the donor? (y/n): ")
        if choice.lower() == 'y':
            for donor in matching_donors:
                donors.remove(donor)
            print("Donor deleted successfully.")
        else:
            print("Deletion aborted.")

def menu():
    donors = read_csv_file('donor.csv')

    while True:
        print("\nMenu:")
        print("1. Display all donors")
        print("2. Search for a donor")
        print("3. Add a new donor")
        print("4. Modify donor details")
        print("5. Delete a donor")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_donors(donors)
        elif choice == '2':
            search_name = input("Enter the donor name to search: ")
            matching_donors = search_donor(donors, search_name)
            display_donors(matching_donors)
        elif choice == '3':
            append_donor(donors)
        elif choice == '4':
            modify_donor(donors)
        elif choice == '5':
            delete_donor(donors)
        elif choice == '6':
            write_csv_file('donor.csv', donors)
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
