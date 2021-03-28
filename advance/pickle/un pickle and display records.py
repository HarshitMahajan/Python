import pickle
emp=[]
f= open('employee.dat','rb')
ans='y'
while True:
    try:
        emp=pickle.load(f)
    except EOFError:
        break
print("%10s"%"EMP NO","%20s"%"EMP NAME","%10s"%"EMP SALARY")
print("**************************************************")
for e in emp:
    print("%10s"%e[0],"%20s"%e[1],"%10s"%e[2])
f.close()
