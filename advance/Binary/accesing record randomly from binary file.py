size_of_rec = 20
num = int(input("enter Record Number:"))
with open('Names.dat','wb') as f:
    f.seek(size_of_rec*(num-1))
    str=f.read(size_of_rec)
    if(len(str)==0):
        print("Incorrect Position")
    else:
        print(str.decode())
        
