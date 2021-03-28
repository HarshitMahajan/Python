import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',password='root',database='class12')
mycursor=mycon.cursor()
mycursor.execute("select*from emp")
print(mycursor)
