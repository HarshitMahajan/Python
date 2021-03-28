1#fibonaci series
a=0
b=1
n=int(input(" How many numbers in series - "))
print(a,b, end=",")
for i in range (3,n+1):
    c=a+b
    print(c,end=" ")
    a,b=b,c
 
