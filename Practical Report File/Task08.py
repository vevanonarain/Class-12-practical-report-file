#Task 08 - 23/6/2023
#Vevan O Narain S7-C 

""" Define a function SumOfFactors(N) to calculate and return sum of all proper factors of N (all
    factors including 1 and excluding the number N itself). Using the defined function, write a
    program to check whether a number M is perfect or not."""
    
def sumOfFactors(n):
    l = []
    
    for i in range(1,  n):
        if n % i == 0:
            l.append(i)
            
    return sum(l)

x = int(input("Enter Number: "))
print(sumOfFactors(x))

if sumOfFactors(x) == x:
    print(f"{x} is a perfect number")
else:
    print(f"{x} is not a perfect number")