import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='root',database='class12')
mycursor=mycon.cursor()
mycursor.execute("select * from emp")
mydata=mycursor.fetchone()
nrec=mycursor.rowcount
print("total records found are",nrec)
print(mydata)
print('=========================')
mydata=mycursor.fetchone()
nrec=mycursor.rowcount
print("total records fetched are",nrec)
print(mydata)
