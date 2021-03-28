string=input("enter a string:")
length=len(string)
print("original string=",string)
string2=""
for a in range(0,length):
    if a%2==0:
        string2+=string[a]
    else:
        string2+=string[a].upper()
print("new string=",string2)
