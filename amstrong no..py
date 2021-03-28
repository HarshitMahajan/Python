# program to check weather number  is a armstrong or not.
num=int(input("enter 3-digit number:"))
f=num
sum=0
while(f>0):
    a=f%10
    f=int(f/10)
    sum=sum+(a**3)
if (sum==num):
    print("it is an amstrong no.:",num)
else:
    print("it is not an amstrong no.:",num)
