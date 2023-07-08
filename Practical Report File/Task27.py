#Task 27 - 27/6/2023
#Vevan O Narain S7-C

"""Write a menu based program to perform the following task on a Python tuple NUMBERS.
A sample tuple NUMBERS = (12, 33, 13, 54, 34, 57)
The tasks are:
i) Add a new number in the tuple NUMBERS, entered by the user
ii) Display all numbers stored in the tuple NUMBERS
iii) Sort the tuple NUMBERS in descending order."""

numbers = (12, 33, 13, 54, 34, 57)

new = 23
numbers = numbers + (new, )

print(numbers)

x = (sorted(numbers))

print(x[::-1])