#Task 30 - 27/6/2023
#Vevan O Narain S7-C

"""Define a function GRADES(EMPLOYEES) to accept a Python dictionary EMPLOYEES as a
formal argument and creates and returns two separate dictionaries GradeA and GradeB
depending upon whether the values(Salary) are more than 25000 or not as explained below:
A sample Dictionary EMPLOYEES = {'John':18000,'Rahim':24000,'Anita':31000}
The separated Dictionaries are:
GradeA = {'Anita':31000}
GradeB = {'John':18000,'Rahim':24000}
The tasks are:
i) Add a new entry in the Dictionary EMPLOYEES, entered by the user
ii) Display all entries stored in the Dictionary EMPLOYEES
iii) Separate the Dictionary EMPLOYEES using the defined function and display the two
newly created Dictionaries GradeA and GradeB."""

def grades(employee):
    gradeA = {}
    gradeB = {}

    for i in employee:
        if employee[i] > 25000:
            gradeA[i] = employee[i]
        else:
            gradeB[i] = employee[i]

    return gradeA, gradeB

employees = {'John': 18000, 'Rahim': 24000, 'Anita': 31000}
new_emp = input("Enter Name: ")
new_sal = int(input("Enter Salary: "))
employees[new_emp] = new_sal

print(f"The employees are: {employees}")
print(f"Grade A and Grade B employees respectively are: {grades(employees)}")