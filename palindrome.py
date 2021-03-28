#program to check weather a number is in palindrome or not
orig=int(input("enter a number: "))
num=orig
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=int(num/10)
if orig==rev:
    print("palindrome")
else:
    print("not a palindrome")
