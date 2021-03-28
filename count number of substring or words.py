#program the counts the no. of substring in a line
str1=input("enter line:")
str2="is"
l=str1.split()
cnt=0
for i in l:
    if i==str2:
        cnt+=1
print("sunstring is appearing:",cnt)
