import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='root',database='class12')
mycursor=mycon.cursor()
mycursor.execute("select * from emp")
mydata=mycursor.fetchall()
nrec=mycursor.rowcount
print("total records found are",nrec)
for a,b,d,f,g,h,c,j in mydata:
    print(a,b,c)
