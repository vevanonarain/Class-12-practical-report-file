#Task 04 - 23/6/2023
#Vevan O Narain S7-C

""" Define a function HCF(A,B) to calculate and return the HCF/GCD of the numbers A and B.
    Using the defined function, write a program to check whether two user inputted M and N are
    co-prime or not."""
    
def hcf(a, b):
    f = []
    
    if a > b:
        for i in range(2, a + 1):
            if (a % i == 0 and b % i == 0):
                f.append(i)
        
    else:
        for i in range(2, b + 1):
            if (a % i == 0 and b % i == 0):
                f.append(i)
                
    if len(f) > 0:
        print(f"These numbers are not co prime. Their HCF is {f[-1]}")
    else:                
        print("These numbers are co prime. Their HCF is 1")
    
num1 = int(input("Enter first natural number: "))
num2 = int(input("Enter second natural number: "))
  
hcf(num1, num2)