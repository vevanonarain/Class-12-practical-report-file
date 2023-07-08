#Task 43 - 1/7/23
#Vevan O Narain S7-C

"""Write a Python program to read each row from a given csv file and print a list of strings."""

import csv

def read_csv_file(filename):
    rows = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)
    return rows

def print_list_of_strings(rows):
    for row in rows:
        print(', '.join(row))

filename = 'myfile.csv'
rows = read_csv_file(filename)
print_list_of_strings(rows)