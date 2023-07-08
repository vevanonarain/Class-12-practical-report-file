#Task 40 - 1/7/23
#Vevan O Narain S7-C

""" A binary file “STUDENT.DAT” has structure [admission_number, Name, Percentage]. Write a 
function countrec() in Python that would read contents of the file “STUDENT.DAT” and display 
the details of those students whose percentage is above 75. Also display number of students 
scoring above 75%."""

import pickle

def countrec():
   fobj = open("student.dat","rb")
   num = 0

   try:
      while True:
         rec = pickle.load(fobj)
         
         if rec[2] > 75:
            num = num + 1
         
         print(rec[0],rec[1],rec[2])
         
   except:
      fobj.close()

   return num

print(countrec())