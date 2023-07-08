#Task 03 - 23/6/2023
#Vevan O Narain S7-C

"""Define a function isPalindrome(N) to check whether N is a Palindromic number or not. If
   Palindrome, the function should return 1 otherwise 0."""

def pallindrome(n):
    x = str(n)
    
    if x == x[::-1]:
        return 1
    else:
        return 0     
    
x = int(input("Enter Number: "))
print(pallindrome(x))