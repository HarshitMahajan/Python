import pickle
emp=[]
f=open('employee.dat','rb')
ans='y'
while True:
    try:
        emp=pickle.load(f)
    except EOFError:
            break
for e in emp:
    print(e)
f.close()
