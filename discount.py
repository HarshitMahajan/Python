#program to check discount
a=int(input("enter amount="))
discount=a/10
total=a-discount
if a>=1000:
    discount=a/10
    total=a-discount
    print("total=",total)
else:
    print("amount=",a)
