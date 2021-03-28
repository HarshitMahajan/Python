#program to read a line and display the number of words in it
line=input("enter line:")
x=line.split()
cnt=0
for i in x:
    cnt=cnt+1
print(cnt)
