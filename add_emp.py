import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',database='company',password='akk@123')
cur=conn.cursor()
eid=int(input("Enter the empid"))
name=input("Enter the name")
salary=float(input("Enter the salary"))
dept=input("Enter your department")
q="insert into emp(empid,name,salary,dept) values(%s,%s,%s,%s)"
val=(eid,name,salary,dept)
cur.execute(q,val)
conn.commit()
print("successfully saved")
