#Program to accept a decimal number and display its binary number
n=int(input("enter no "))
a=0
m=0
c=1
while n>0:
    a=n%2
    m=m+(a*c)
    c=c*10
    n=int(n/2)
print(m)
