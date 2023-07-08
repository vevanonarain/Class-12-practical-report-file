#Task 16 - 24/6/2023
#Vevan O Narain S7-C

"""WAPP to process STACK (LIFO) operations on a Python LIST of numbers"""

stack = []
 
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
