import mysql.connector as mys
#PROGRAM FOR DATABASE CONNECTIVITY
def connect():
    db= mysql.connector.connect(host='localhost',user='root',password='root',database='schoolmanagement')
    if db.is_connected==True:
       print("connected")
    return db

#PROGRAM FOR USING SCHOOL MANAGEMENT   

def select():
    print("-----------------------WELCOME TO SCHOOL MANAGEMENT-------------------------")
    print("1.STUDENT MANAGEMENT")
    print("2.EMPLOYEE MANAGEMENT")
    print("3.DISPLAY FEE")
    print("4.ATTENDANCE MANAGEMENT")
    print("5.DISPLAY SCHOOL DETAILS")
    
    ch=int(input("enter your choice(1-5):-"))
    if ch==1:
        print("\n------------------WELCOME TO STUDENT MANAGEMENT------------------\n")
        print("a.NEW ADMISSION")
        print("b.UPDATE DETAILS")
        print("c.ISSUE TC")
        print("\nEXISTING RECORDS ARE\n")
        def displayst():
              con=connect()
              cur=con.cursor()
              cur.execute("select * from st")
              for i in cur.fetchall():
                admno=i[0]
                name=i[1]
                clas=i[2]
                city=i[3]
                dob=i[4]
                print("(admno=%d,name=%s,class=%s,city=%s,dob=%s)"%(admno,name,clas,city,dob))
        displayst()
        c=input("enter your choice(a-c):-")
        if c=='a': 
          def insertst():
              name=input("enter student name:-")
              admno=int(input("enter admission number:-"))
              clas=input("enter class:-")
              city=input("enter city:-")
              dob=input("enter date of birth(year-month-time):-")
              con=connect()
              cur=con.cursor()
              cur.execute("insert into st(name,admno,class,city,dob)values('%s','%d','%s','%s','%s')"%(name,admno,clas,city,dob)) 
              con.commit()        

          insertst()
          print("MODIFIED RECORDS ARE")
          displayst()
          
          
        elif c=='b':
            def updatest():
                con=connect()
                cur=con.cursor()
                clas=input("ENTER NEW CLASS:-")
                admno=int(input("ENTER ADMISSION NO. :-"))
                cur.execute("update st set class=%s where admno=%d"%(clas,admno))
                con.commit()
                
                
            updatest()
            print("\nMODIFIED DETAILS ARE:-\n")
            displayst()
        elif c=='c':
            def deletest():
                con=connect()
                cur=con.cursor()
                admno=int(input("ENTER ADMISSION NO. TO BE DELETED:-"))
                ans=input("ARE YOU SURE YOU WANT TO DELETE(y/n):-")
                if ans=='y' or ans=='Y':
                    cur.execute("delete from st where admno=%d"%(admno))
                    con.commit()
                    
            deletest()
            print("\nMODIFIED DETAILS ARE:-\n")
            displayst()
     
    elif ch==2:
        print("/n------------------WELCOME TO EMPLOYEE------------------/n")
        print("a. NEW EMPLOYEE")
        print("b. UPDATE STAFF DETAILS")
        print("c. DELETE EMPLOYEE")
        e=input("enter your choice(a-c)")
        print("\nEXISTING RECORDS ARE\n")
        def displayemp():
            con=connect()
            cur=con.cursor()
            cur.execute("select * from emp")
            for i in cur.fetchall():
                empno=i[0]
                name=i[1]
                job=i[2]
                hiredate=i[3]
                print("(empno=%d,name=%s,job=%s,hiredate=%s)"%(empno,name,job,hiredate))
                
        displayemp()       
        if e=='a':   
            def insertemp():
              empno=int(input("enter empno:-"))
              name=input("enter employee name:-")
              job=input("enter designation:-")
              hiredate=input("enter hiredate(year-month-time):-")
              con=connect()
              cur=con.cursor()
              cur.execute("insert into emp(empno,name,job,hiredate)values('%d','%s','%s','%s')"%(empno,name,job,hiredate)) 
              con.commit()
              
            insertemp()  
                        
            def displayemp():
              con=connect()
              cur=con.cursor()
              cur.execute("select * from emp")
              for i in cur.fetchall():
                empno=i[0]
                name=i[1]
                job=i[2]
                hiredate=i[3]
                print("(empno=%d,name=%s,job=%s,hiredate=%s)"%(empno,name,job,hiredate)) 
            
            print("\nMODIFIED RECORDS ARE\n")
            displayemp()
        elif e=='b':
            def updateemp():
                con=connect()
                cur=con.cursor()
                job=input("ENTER NEW JOB:-")
                empno=int(input("ENTER EMPLOYEE NO:-"))
                cur.execute("update emp set job='%s' where empno=%d"%(job,empno))
                con.commit()
                
                
                
            updateemp()    
            print("\nMODIFIED RECORDS ARE\n")
            displayemp()
        elif e=='c':
            def deleteemp():
                con=connect()
                cur=con.cursor()
                d=int(input("ENTER EMPNO TO BE DELETED:-"))
                ans=input("ARE YOU SURE YOU WANT TO DELETE RECORD(y/n):-")
                if ans=='y' or ans=='Y':
                    cur.execute("delete from emp where empno=%d"%(d))
                    con.commit()
                    
            deleteemp()
            print("\nMODIFIED RECORDS ARE\n")
            displayemp()    
    
       
         
    elif ch==3:
        print("\n--------------WELCOME TO DISPLAY FEES------------------\n")
        print("a.INSERT FEES")
        print("b.UPDATE FEES")
        print("c.EXEMPT FEES")
        print("\n EXISTING RECORDS ARE:-\n")
        def displayfee():
            con=connect()
            cur=con.cursor()
            cur.execute("select * from fees")
            for i in cur.fetchall():
                admno=i[0]
                fees=i[1]
                monthunpaid=i[2]
                print("(admno=%d,fees=%f,monthunpaid=%s)"%(admno,fees,monthunpaid))
        

        displayfee()        
                
        f=input("ENTER YOUR CHOICE(a-c):-")
        if f=='a':
            def insertfee():
                admno=int(input("ENTER ADMISSION NO. :-"))
                fees=float(input("ENTER AMOUNT OF FEES TO BE PAID:-"))
                monthunpaid=input("ENTER MONTH OF WHICH FEES TO BE PAID:-")
                con=connect()
                cur=con.cursor()
                cur.execute("insert into fees(admno,fees,monthunpaid) values ('%d','%f','%s')"%(admno,fees,monthunpaid))
                con.commit()
                
                
                
            insertfee()    
            print("\nMODIFIED RECORDS ARE:-\n")
            displayfee()
            
            
        elif f=='b':
            def updatefee():
                month=input("ENTER MONTH TO BE UPDATED:-")
                admno=int(input("ENTER ADMISSION NO.:-"))
                con=connect()
                cur=con.cursor()
                cur.execute("update fees set monthunpaid='%s'where admno=%d"%(month,admno))
                con.commit()
            
                
            
            updatefee()
            print("\nMODIFIED RECORDS ARE\n")    
            displayfee()    
            
            
        elif f=='c':
            def deletefee():
                admo=int(input("ENTER ADMISSION NO.:-"))
                a=input("ENTER ARE YOU SURE YOU WANT TO EXEMPT FEE(y/n):-")
                con=connect()
                cur=con.cursor()
                if a=='Y' or a=='y':
                    cur.execute("delete from fees where admno=%d"%(admo))
                    con.commit()
                    
            
            deletefee()
            print("\nMODIFIED RECORDS ARE\n")
            displayfee()
                
    elif ch==4:
        print("\n------------------WELCOME TO ATTENDANCE MANAGEMENT------------------\n")
        print("a.INSERT DETAILS")
        print("b.UPDATE DETAILS")
        print("c.DELETE DETAILS")
        print("\nEXISTING DETAILS ARE:-")
        def displayatt():
            con=connect()
            cur=con.cursor()
            cur.execute("select * from attendance")
            for i in cur.fetchall():
                admno=i[0]
                name=i[1]
                present=i[2]
                totalpresent=i[3]
                per=i[4]
                print("(admno=%d,name=%s,present=%d,totalpresent=%d,per=%f)"%(admno,name,present,totalpresent,per))
        displayatt()        
        a=input("enter your choice")
        if a=='a':
            def insertatt():
                admno=int(input("ENTER ADMISSION NO.:-"))
                name=input("ENTER STUDENT NAME:-")
                present=int(input("ENTER CLASS ATTENDED DURING THE YEAR:-"))
                totalpresent=int(input("ENTER TOTAL CLASS ATTENDED DURING THE YEAR:-"))
                per=float(input("ENTER PERCENTAGE:-"))
                con=connect()
                cur=con.cursor()
                cur.execute("insert into attendance(admno,name,present,totalpresent,per) values ('%d','%s','%d','%d','%f')"%(admno,name,present,totalpresent,per))
                con.commit()
            
            insertatt()
            print("\nMODIFIED DETAILS ARE:-\n")
            displayatt()
         
        elif a=='b':
            def updateatt():
                present=int(input("ENTER CLASS ATTENDED DURING THE YEAR:-"))
                per=float(input("ENTER PERCENTAGE:-"))
                admno=int(input("ENTER ADMISSION NO.:-"))
                con=connect()
                cur=con.cursor()
                cur.execute("update attendance set present='%d',per='%f' where admno='%d'"%(present,per,admno))
                con.commit()
          
            updateatt()
            print("\nMODIFIED DETAILS ARE:-\n")
            displayatt()
            
        elif a=='c':
            def deleteexam():
                admno=int(input("ENTER ADMISSION NO.:-"))
                f=input("ARE YOU SURE YOU WANT TO DELETE(y/n):-")
                con=connect()
                cur=con.cursor()
                if f=='y' or f=='Y':
                    cur.execute("delete from attendance where admno='%d'"%(admno))
                    con.commit()
                    
            deleteexam()
            print("\nMODIFIED DETAILS ARE:-\n")
            displayatt()
    
    elif ch==5:
        print("\n------------------WELCOME TO DISPLAY  SCHOOL RELATED DETAILS------------------\n")
        print("a.INSERT DETAILS")
        print("b.UPDATE DETAILS")
        print("c.DELETE DETAILS")
        print("\nEXISTING DETAILS ARE:-\n")
        def displaysc():
            con=connect()
            cur=con.cursor()
            cur.execute("select * from school")
            for i in cur.fetchall():
                sid=i[0]
                sname=i[1]
                noofstudent=i[2]
                noofemployee=i[3]
                nooflabs=i[4]
                print("(id=%d,sname='%s',noofstudent=%d,noofemployee=%d,nooflabs=%d)"%(sid,sname,noofstudent,noofemployee,nooflabs))
          
                  
        displaysc()
        s=input("ENTER YOUR CHOICE")
        if s=='a':
            def insertsc():
                sid=int(input("ENTER SCHOOL ID:-"))
                sname=input("ENTER SCHOOL NAME:-")
                noofstudent=int(input("ENTER NUMBER OF STUDENT:-"))
                noofemployee=int(input("ENTER NUMBER OF EMPLOYEE:-"))
                nooflabs=int(input("ENTER NUMBER OF LABS:-"))
                con=connect()
                cur=con.cursor()
                cur.execute("insert into school(id,sname,noofstudent,noofemployee,nooflabs)values(%d,'%s',%d,%d,%d)"%(sid,sname,noofstudent,noofemployee,nooflabs))
                con.commit()
             
            insertsc()
            print("\nMODIFIED DETALIS ARE:-\n")
            displaysc()
            
            
        elif s=='b':
            def updatesc():
                noofstudent=int(input("ENTER NUMBER OF STUDENT:-"))
                noofemployee=int(input("ENTER NUMBER OF EMPLOYEE:-"))
                nooflabs=int(input("ENTER NUMBER OF LABS:-"))
                sid=int(input("ENTER SCHOOL ID:-"))
                con=connect()
                cur=con.cursor()
                cur.execute("update school set noofstudent=%d,noofemployee=%d,nooflabs=%d where id=%d"%(noofstudent,noofemployee,nooflabs,sid))
                con.commit()
                
            updatesc()
            print("\nMODIFIED DETALIS ARE:-\n")
            displaysc()
            
        elif s=='c':
            def deletesc():
                sid=int(input("ENTER SCHOOL ID:-"))
                con=connect()
                cur=con.cursor()
                cur.execute("delete from school where id=%d"%(sid))
                con.commit()
            
            
            deletesc()
            print("\nMODIFIED DETALIS ARE:-\n")
            displaysc()
    elif ch==6:
        print("\n -----------------WELCOME TO EXTRA CURRICULARS----------------------------\n")
        print("a.NEW EXTRA CURRICULAR ACTIVITY:-")
        print("b.EXISTING CURRICULAR ACTIVITY:-")
        def displayeca():
            con.connect()
            cur=con.connect()
            cur.execute("select*form eca")
            
             
         
    d=input("DO YOU WANT TO USE THE DATABASE AGAIN(y/n)")
    if d=='y'or d=='Y':
        select()
    elif d=='n' or d=='N':
        print("\n------------------THANKS FOR VISITING SCHOOL MANAGEMENT------------------\n")
         
       
select()        
