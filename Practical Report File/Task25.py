#Task 25 - 24/6/2023
#Vevan O Narain S7-C

"""WAPP to create a Python LIST-STUDENTS contains 10 small LISTs storing names 
and respective marks of few students.  Display only those student's name who have 
scored 60 or more."""

l = []

for i in range(10):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    x = [name, marks]

    l.append(x)

for i in l:
    if i[1] >= 60:
        print(f"{i[0]}:{i[1]}")
