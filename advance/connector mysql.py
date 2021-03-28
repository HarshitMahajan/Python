import mysql.connector 
mydb = mysql.connector.connect (
    host='localhost',
    user='root',
    password='root',
    database='class12'
)
if mydb.is_connected():
    print("sucessfully conneted")
