#Task 17 - 24/6/2023
#Vevan O Narain S7-C

"""WAPP to process QUEUE (FIFO) operations on a Python LIST of names"""

queue = []
  
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Initial queue")
print(queue)
  
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)
