#Task 23 - 24/6/2023
#Vevan O Narain S7-C

"""Write a menu (and function) based program to perform the following tasks on a Python List
STUDENTS storing name and marks of few students having the following structure and
implemented as a Stack based on LIFO operations.

A sample List STUDENTS=[['Raghav',89],['Rohan',90],['Amrita',91]]

The tasks are (based on LIFO):
i) Add a new student in the List STUDENTS, name and marks entered by the user
ii) Display all Student's Names and their Marks from the List STUDENTS
iii) Remove a student from the List STUDENTS. Also display the content of the removed
student. If removal/deletion is not possible, specify the reasons. """

students = [['Raghav',89],['Rohan',90],['Amrita',91]]

name = input("Enter Name: ")
marks = int(input("Enter Marks: "))
l = [name, marks]
students.append(l)

print(f"List of students: {students}")

try:    
    print(f"Removed student: {students.pop()}")
except:
    print('Stack overflow! The list is empty!')



