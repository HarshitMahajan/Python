import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='root',database='class12')
mycursor=mycon.cursor()
mycursor.execute("select * from emp")
mydata=mycursor.fetchone()
nrec=mycursor.rowcount
print("total records found are",nrec)
mydata=mycursor.fetchone()
nrec=mycursor.rowcount
print("total records fetched are",nrec)
mydata=mycursor.fetchmany (2)
nrec=mycursor.rowcount
print("total records fetched are",nrec)

