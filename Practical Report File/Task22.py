#Task 22 - 24/6/2023
#Vevan O Narain S7-C

"""WAPP to to print duplicates from a list of integers"""

l = []

for i in range(10):
    num = input("Enter Number: ")
    l.append(num)
 
uniqueList = []
duplicateList = []
 
for i in l:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)