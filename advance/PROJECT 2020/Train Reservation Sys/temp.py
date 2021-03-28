import mysql.connector as ch
conn=ch.connect(host='localhost',user="root",passwd='1234',database='chirag')
#if conn.is_connected()==1:
#    print("connected")
#else:
#    print("not connected")

cur=conn.cursor()
i=0
def railsmenu():
                print("Railway Reservation ")
                print("1.Train Detail")
                print("2.Reservation of Ticket")
                print("3.Cancellation of Ticket")
                print("4.Display PNR status")
                print("5.Quit")
                print("6.For adding in train detal")
                
                n=int(input("Enter your choice"))
                if(n==1):
                                train_detail()
                elif(n==2):
                                reservation()
                elif(n==3):
                                cancel()
                elif(n==4):
                                displayPNR()
                elif(n==5):
                                return("exit")
                elif (n==6):
                                train()
                else:
                                print("wrong choice")

def train_detail():
    l=[]
    a=str(input("Enter your starting point:"))
    b=str(input("Enter your destination:"))
    l.append(a)
    l.append(b)
    sql="select train_no,cost,via,time_of_departure,date_available from train_detail where starting_point=%s and destination=%s"
    cur.execute(sql,l)
    f=cur.fetchall()
    l=len(f)
    for j in range(0,l):
        print("information u need resp as train_no,cost,via,time of departure,date availaible",j+1,":",f[j])
    print(railsmenu())
def reservation():
    print("1. Enter YOUR INFORMATION AS FOLLOWS:")
    l=[]
    l1=[]
    l2=[]
    global i
    l.append(i)
    i=i+1
    a=str(input("Enter passenger's name:"))
    l.append(a)
    
    b=str(input("Enter your age:"))
    l.append(b)
    c=str(input("Enter your gender M/F/O:"))
    l.append(c)
    d=str(input("Enter train_no:"))
    l.append(d)
    l1.append(d)
    l2.append(d)
    e="select starting_point,destination from train_detail where train_no=%s"
    cur.execute(e,l1)
    f=cur.fetchall()
#    print(f)
    w=f[0]
    x=w[0]
    t=w[1]
    print(x)
    print(t)
#    l.append(w)
    l.append(x)
    l.append(t)
#    l.append(f)
#    print(l)
#    print(cur.fetchall())
#    h=float(input("date on which u want to travel(dd.mm):"))
#    l.append(h)
#    print(l)
    g="insert into user_information(unique_id,uname,age,gender,train_no,starting_point,destination)values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(g,l)
    conn.commit()
    print("information uploaded")
    Z="select cost from train_detail where train_no=%s"
    cur.execute(Z,l1)
    n=cur.fetchall()
    print("you have to pay:",n)
    mn=str(input("would you like to confirm your seat(y/n):"))
    l3=[]
    l4=[]
    pop="reserved"
    dop="not reserved"
    l3.append(pop)
    l4.append(dop)
    l5=l3+l1
    l6=l4+l1
    
    if mn=="y":
        print("your ticket is confirmed")
        print("in case of cancellation your unique_id is :",i-1)
        mysql="update user_information set reservation=%s where train_no=%s"
        cur.execute(mysql,l5)
        conn.commit()
        print("your ticket is confirmed")
    elif mn=="n":
        print("your ticket is not reserved")
        mysql="update user_information set reservation=%s where train_no=%s"
        cur.execute(mysql,l6)
        conn.commit()
    else:
        print("wrong option")
        print(railsmenu())
        
    print(railsmenu())
def cancel():
    l=[]
    q="not reserved"
    l.append(q)
    a=int(input("Enter Value Of Your Unique_id Provided:"))
    l.append(a)
    b="update user_information set reservation=%s where unique_id=%s"
    cur.execute(b,l)
    conn.commit()
    print("YOUR TICKET IS CANCELLED")
    
def displayPNR():
    l=[]
    a=int(input("Enter Value Of Your Unique_id Provided:"))
    l.append(a)
    sql="select * from user_information where unique_id=%s"
    cur.execute(sql,l)
    f=cur.fetchall()
    print("your current reservation status is:",f)
    
def train():
    print("Train Details")
    ch='y'
    while (ch=='y'):
                    l=[]
                    tnum=int(input("Enter Train_no :"))
                    l.append(tnum)
                    ac1=float(input("Enter Train cost: "))
                    l.append(ac1)
                    ac2=str(input("Enter Starting_point Of Train:"))
                    l.append(ac2)
                    ac3=str(input("Enter train's destination:"))
                    l.append(ac3)
                    slp=str(input("Enter via:"))
                    l.append(slp)
                    e=str(input("Enter time of departure of train:"))
                    l.append(e)
                    f=str(input("Enter the date of train board:"))
                    l.append(f)
                    sql="insert into train_detail values(%s,%s,%s,%s,%s,%s,%s)"
                    print(sql,l)
                    cur.execute(sql,l)
                    conn.commit()
                    print("insertion completed")
                    print("Do you want to insert more train Detail")
                    ch=input("Enter y/n")
    print('\n' *10)

    print("===================================================================")
    railsmenu()

#def exit():
#    return
print(railsmenu())
    
    