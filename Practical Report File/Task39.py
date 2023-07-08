#Task 39 - 1/7/23
#Vevan O Narain S7-C

"""A binary file “salary.DAT” has structure [employee id, employee name, salary]. Write 
a function countrec() in Python that would read contents of the file “salary.DAT” and 
display the details of those employee whose salary is above 20000."""

def countrec():
    num = 0
    fobj = open("data.dat","rb")
    
    try:
        print("Emp id\tEmp Name\tEmp Sal")

        while True:
            rec = pickle.load(fobj)
            if rec[2] > 20000:
                print(rec[0],"\t\t",rec[1],"\t\t",rec[2])
    except:
        fobj.close()
countrec()