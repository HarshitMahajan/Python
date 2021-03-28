import pickle
emp=[]
f = open('employee.dat','wb')
ans='y'
while ans=='y':
    eno=int(input("enter Employee Number:"))
    name= input("enter Employee Nme")
    salary=int(input("Enter Salary"))
    emp.append([eno,name,salary])
    ans=input("add More recrd")
pickle.dump(emp,f)
f.close()
