#Task 33 - 30/6/23
#Vevan O Narain S7-C

"""WAPP to read lines from a text file INDIA.TXT to find 
and display the occurrence of the word 'India'."""

def count_word():
    file = open('india.txt','r')
    count = 0

    for line in file:
        words = line.split()
        for word in words:
            if word == 'India':
                count += 1
        print(count)

    file.close()

count_word()