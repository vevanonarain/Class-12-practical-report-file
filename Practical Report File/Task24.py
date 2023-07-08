#Task 24 - 24/6/2023
#Vevan O Narain S7-C

"""Write a menu (and function) based program to perform the following tasks on a Python List
PERSONS storing name and age of few persons having the following structure and
implemented as a Queue based on FIFO operations.

A sample List PERSONS=[['Rahamat',18],['Rajeev',19],['Amos',17]]

The tasks are (based on FIFO):
i) Add a new person in the List STUDENTS, name and age entered by the user
ii) Display all person’s Names and their Age from the PERSONS List
iii) Remove a person from the List PERSONS. Also display the content of the removed
person. If removal/deletion is not possible, specify the reasons. """

students = [['Rahamat',18],['Rajeev',19],['Amos',17]]

name = input("Enter Name: ")
age = int(input("Enter age: "))
l = [name, age]
students.append(l)

print(f"List of students: {students}")

try:    
    print(f"Removed student: {students.pop(0)}")
except:
    print('Stack overflow! The list is empty!')

