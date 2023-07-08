#Task 34 - 30/6/23
#Vevan O Narain S7-C

"""Write a function in Python to count and display number of vowels in text file"""

def count_vowels():
    infile = open('first.txt','r')
    count = 0
    data = infile.read()
    for letter in data:
        if letter in 'aeiouAEIOU':
            count += 1

    print('Number of vowels are',count)            
    infile.close()

count_vowels()