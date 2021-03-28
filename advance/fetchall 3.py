import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='root',database='class12')
mycursor=mycon.cursor()
mycursor.execute("select * from emp")
mydata=mycursor.fetchall()
nrec=mycursor.rowcount
print("total records found are",nrec)
for row in mydata:
    print(row[0],':',row[1],':',row[2],':',row[3],':')
