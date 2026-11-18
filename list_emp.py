import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',database='company',password='akk@123')
cur=conn.cursor()
print("List of employees")
print('-'*70)
print("%10s %15s %10s %15s"%("EMPID","NAME","SALARY","DEPT"))
print('-'*70)
q="select * from emp"
cur.execute(q)

for row in cur:
    print("%10s %15s %10s %15s"%(row[0],row[1],row[2],row[3]))
