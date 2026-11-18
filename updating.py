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
    ans=input('Update it y/n?')
    if ans=='y':
        print('ENTER NEW DATA')
        print('-'*20)
        name=input('Enter new name:')
        sal=int(input('Enter new salary:'))
        d=input('Enter new dept:')
        conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='company')
        cur=conn.cursor()
        q='update emp set name=%s, salary=%s, dept=%s where empid=%s'
        val=(name,sal,d,n)
        cur.execute(q,val)
        conn.commit()
        print('Successfully updated')
        
    
