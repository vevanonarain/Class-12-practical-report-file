#Task 10 - 23/6/2023
#Vevan O Narain S7-C 

""" Define a function isPerfect(N) to check whether N is a perfect or not. If perfect, the function
    should return 1 otherwise 0. Using the defined function, write a program to display all perfect
    numbers between 1 and 1000.""" 

    
def isPerfect(n):
    d = []
    
    for i in range(1, n):
        if n % i == 0:
            d.append(i)
            
    if n == 1:
        return 1
    elif sum(d) == n:
        return 1
    else:
        return 0
    
n = int(input("Enter Number: "))
print(f"{n}: {isPerfect(n)}")

print("Perfect Numbers between 1 and 1000 are: ")

for i in range(1, 1001):
    if isPerfect(i) == '1':
        print(i, end = ', ')