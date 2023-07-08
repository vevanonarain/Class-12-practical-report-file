#Task 11 - 23/6/2023
#Vevan O Narain S7-C
 
"""Define a recursive function Fibonacci(N) to calculate and return Nth member of the Fibonacci
number series. Write a program to display the first 20 Fibonacci numbers."""

def fibo(n):
    l = [0, 1]
    a = 0
    b = 1
    for i in range(1, n + 1):
        c = a + b
        l.append(c)
        a = b
        b = c
    
    return l

x = int(input("Enter Number: "))
print(fibo(x))