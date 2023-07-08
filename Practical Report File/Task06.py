#Task 06 - 23/6/2023
#Vevan O Narain S7-C

"""Define a function to read a name and display the initials as M.K.G"""

def name(str):
    x = str.split()
    l = []

    for i in x:
        initials = i[0]
        l.append(initials)

    print(*l, sep = '.')

string= input("Enter Name: ")
name(string)