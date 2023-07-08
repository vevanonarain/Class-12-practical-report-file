#Task 13 - 23/6/2023
#Vevan O Narain S7-C

"""Define a function to find the LCM of two numbers"""

def calculate_lcm(x, y):  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while True:  
        if greater % x == 0 and greater % y == 0:  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
   
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  

print(f"The L.C.M. of {num1} and {num2} is {calculate_lcm(num1, num2)}")  