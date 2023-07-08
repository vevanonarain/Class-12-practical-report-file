#Task 29 - 27/6/2023
#Vevan O Narain S7-C

"""Define a function FREQTable(S) which accepts a string S, having a sentence of few words.
The function creates a Dictionary FT to store the frequency table of individual words in the
sentence STR. Function finally returns the Dictionary FT.
Note: While creating FT, ignore the space.
If STR= 'INDIANA'
The function should return FT={'I':2, 'N':2, 'D':1, 'A':2}
Write a minimal program to use the defined function effectively"""

d = {}

str = input("Enter String: ")

for i in str:
    d[i] = str.count(i)

print(d)