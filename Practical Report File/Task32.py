#Task 32 - 30/6/23
#Vevan O Narain S7-C

"""Write a function in Phyton to read lines from a text file diary.txt 
and display only those lines, which are starting with an alphabet P"""

def readlines():
    file = open('diary.txt','r')
    for line in file:
        if line[0] == 'P':
            print(line)

    file.close()

readlines()