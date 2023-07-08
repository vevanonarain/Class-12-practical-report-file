#Task 31 - 30/6/23
#Vevan O Narain S7-C

"""WAPP to write multiple line of text contents into a text file myfile.txt"""

def writelines():
    outfile = open('myfile.txt','w')

    while True:
        line = input('Enter line: ')
        line += '\n'
        outfile.write(line)
        choice = input('Are there more lines y/n? ')
        if choice == 'n':
            break
    outfile.close()

writelines()