#Task 18 - 24/6/2023
#Vevan O Narain S7-C

"""Create a list STUDENT which contains name and marks of students. Create another list 
STACK into which you can push items from student. Also make pop and and display functions."""

STUDENT = [['Gautum', 65], ['Vevan', 70]]
STACK = []

def PUSH():
    for i in STUDENT:
        if i[1] >= 33:
            l.append(i[0])

def POP():
    while len(STUDENT) > 0:
        for i in range(len(STUDENT) - 1, -1, -1):
            print(STUDENT.pop(i))
    else:
        print("Underflow!")

def DISPLAY():
    for i in range(len(STACK) -1, -1, -1):
        print(STACK[i])

while True:
    print("""Operations on Stack:
    1. Push
    2. Pop
    3. Display
    4. Quit
    \n""")

    choice = input("Enter operation you want to be executed: ")

    if choice == "1":
        PUSH()
    elif choice == "2":
        POP()
    elif choice == "3":
        DISPLAY()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")