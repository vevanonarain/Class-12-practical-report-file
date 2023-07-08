#Task 05 - 23/6/2023
#Vevan O Narain S7-C

"""Define functions Pow(X,N) and Factorial(N) to calculate and return XN and N! respectively.
Using the defined function, write programs to calculate and display the sum of following series:
1 + x + x^2 + x^3 ... + x^n."""

def series(n, x):
    sum = 0
    for i in range(n + 1):
        term = x ** i   
        sum += term
        
    return term

a = int(input("Enter n: "))
b = int(input("Enter x: "))

print(series(a, b))