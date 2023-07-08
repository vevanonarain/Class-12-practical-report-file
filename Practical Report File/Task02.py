#Task 02 - 23/6/2023
#Vevan O Narain S7-C

"""Define a function isArmstrong(N) to check whether N is a Armstrong or not. If Armstrong, the
   function should return 1 otherwise 0."""

def armstrong(n):
    s = str(n)
    l = []
    c = []
    
    for i in range(len(s)):
        l.append(int(s[i]))
    
    for i in l:
        cube = i ** 3
        c.append(cube)
        
    if sum(c) == n:
        return 1
    else:
        return 0
    
x = int(input("Enter Number: "))
print(armstrong(x))