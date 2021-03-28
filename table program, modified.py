#to print table of a given no.
n=int(input("enter no whose table you want to print= "))
t=int(input("enter no from where you want to print table="))
m=int(input("enter no till where you want to print table="))
for i in range (t,m):
    table=n*i
    print(n,"*",i,"=",table)
