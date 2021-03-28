#concatenating variable with query
import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='root',database='class12')
mycursor=mycon.cursor()
e=int(input("enter employee number to search"))
query="select * from emp where empno="+str(e)
mycursor.execute(query)
data=mycursor.fetchone()
if data!=None:
    print(data)
else:
    print("no such employee number")
