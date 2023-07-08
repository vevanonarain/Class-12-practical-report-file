#Task 35 - 30/6/23
#Vevan O Narain S7-C

"""Write a menu based python program to display, append and count words in a text file"""

def TXT_DISPLAY():
    f = open("file.txt", "r")
    r = f.read()
    print(r)
    f.close()

def TXT_APPEND():
    f = open("file.txt", "a")
    w = input("Enter the sentence you want to add: ")
    w = w + "\n"
    f.write(w)
    f.close()

def TXT_COUNT():
    file = open('file.txt','r')
    w = input("Enter word: ")
    count = 0

    for line in file:
        words = line.split()
        for word in words:
            if word.lower() == w.lower():
                count += 1
    print(count)

    file.close()

while True:
    print("\nText file Operations:\n1)Display\n2)Append\n3)Word Count\n4)Quit")
    choice = input("Operation you want to choose(1, 2, 3 or 4): ")
    
    if choice == "1":
        TXT_DISPLAY()
    elif choice == "2":
        TXT_APPEND()
    elif choice == "3":
        TXT_COUNT()
    elif choice == "4":
        print("Exiting Program....")
        break
    else:
        print("Invalid argument")