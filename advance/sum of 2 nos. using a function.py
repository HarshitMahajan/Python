#program to add 2 no. using a function
def calsum(x,y):
    s=x+y
    return s

num1=float(input("enter 1st no.="))
num2=float(input("enter 2nd no.="))
sum=calsum(num1,num2)
print("sum of 2 nos.=",sum)
