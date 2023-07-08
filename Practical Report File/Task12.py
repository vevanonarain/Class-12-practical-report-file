#Task 12 - 23/6/2023
#Vevan O Narain S7-C

"""Define a recursive function (N) to calculate and return  of N. Write a program
to display factorial of the first 5 natural numbers."""

def fact(v):
    if v == 0 or v == 1:
        return 1
    return v * (v - 1)

for i in range(1, 6):
    print(fact(i))