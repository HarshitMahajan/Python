#program to serch any name in fie and display the record
#number that contains the name
import os
size_of_rec = 20
# finding size of the file
size = os.path.getsize(name)
print("size of file: ",size)

#finding the number of records
num_rec = int(size/size_of_rec)
print("number of records :",num_rec)

with open("name","rb") as f:
    n = input("enter name to search=")
    n = n.encode()
    position=0
    found = false
    for i in range(num_rec):
        f.seek(position)
        str=f.read(20)
        if n in str:
            print("found at record#",(i+1))
            found=true
        position+=size_of_rec
    if not found:
        print("name not found")
