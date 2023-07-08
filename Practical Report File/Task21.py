#Task 21 - 24/6/2023
#Vevan O Narain S7-C

""" Write a Python program to read a list of numbers and create 2 separate
    lists even and odd. """

str = input("Enter a list of numbers separated by commas: ")
list = str.split(", ")
even = []
odd = []

for num in list:
    if (int(num) % 2 == 0):
        even.append(num)
    else:
        odd.append(num)

print("Odd number(s) is/are ", end="")
print(*odd, sep=", ", end=".")
print()
print("Even number(s) is/are ", end="")
print(*even, sep=", ", end=".")
