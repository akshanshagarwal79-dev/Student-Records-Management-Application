import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='company')
n=int(input("Enter empid"))
cur=conn.cursor()
q="select * from emp where empid=%s"
val=(n,)
cur.execute(q,val)
row=cur.fetchone()
if row==None:
        print("Not Found")
else:
    print("empid: %s"%row[0])
    print("name : %s"%row[1])
    print("salary: %s"%row[2])
    print("dept: %s"%row[3])
    ans=input('Delete it y/n?')
    if ans=='y':
        conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='company')
        cur=conn.cursor()
        q='delete from emp where empid=%s'
        val=(n,)
        cur.execute(q,val)
        conn.commit()
        print('Record has been deleted')
        
    
