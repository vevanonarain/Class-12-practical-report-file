#Task 38 - 1/7/23
#Vevan O Narain S7-C

"""Write a code that reads from a file “sales.dat” which has following information 
[itemcode, amount] and read from the file and find the sum of the amount."""

import pickle

F1 =  open ("sales.dat", "rb")
sum = 0

while True:
    try:
        l = pickle.load(F1)
        sum = sum + l[1]
    except:
        break

print (sum)
F1.close()