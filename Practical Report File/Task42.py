#Task 42 - 1/7/23
#Vevan O Narain S7-C

"""WAPP to create/append a CSV file phone.csv having names and phone numbers of few persons
and to read/search and display the content of the CSV file phone.csv"""

import csv

outFile = open("phone.csv", "a")

RO = csv.writer(outFile)
RO.writerow(["Name", "Phone"])

while True:
    name = input("Enter name: ")
    phone = int(input("Enter phone: "))
    data = [name, phone]

    RO.writerow(data)
    choice = input("Do you want to add more names and marks(Y/N): ")
    if choice.lower() == 'n':
        break

outFile.close()

inFile = open("phone.csv", "r", newline = "\r\n")
listRows = csv.reader(inFile)

for aRow in listRows:
    print(f"{aRow[0]} \t {aRow[1]}")

inFile.close()