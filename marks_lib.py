
from colorama import *
from os import *
import mysql.connector

    
def marks_entry():
    system('color 5f')
    system('cls')
    print("ADD NEW STUDENT")
    print("-"*60)
    rno=int(input("Enter the rollno:"))

    conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
    cur=conn.cursor()
    q="select * from student where rollno=%s"
    val=(rno,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print("Not Found")
    else:
        name=input("Enter the name:")
        fname=input("Enter the father name:")
        clsname=input("Enter the class:")
        section=input("Enter the section:")
        s1=input("Enter the name of first subject:")
        m1=int(input("Enter the marks of first subject:"))
        s2=input("Enter the name of  second subject:")
        m2=int(input("Enter the marks of second subject:"))
        s3=input("Enter the name of  third subject:")
        m3=int(input("Enter the marks of third subject:"))
        s4=input("Enter the name of  fourth subject:")
        m4=int(input("Enter the marks of fourth subject:"))
        s5=input("Enter the name of  fifth subject:")
        m5=int(input("Enter the marks of fifth subject:"))
        conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
        cur=conn.cursor()
        total=m1+m2+m3+m4+m5
        per=total*100/500
        if per>=80:
            grade='A'
        elif per>=60:
            grade='B'
        elif per>=40:
            grade='C'
        else:
            grade='F'
        q="insert into marks(rollno,name,father_name,class,section,subject1,marks1,subject2,marks2,subject3,marks3,subject4,marks4,subject5,marks5,total_marks,percentage,grade) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(rno,name,fname,clsname,section,s1,m1,s2,m2,s3,m3,s4,m4,s5,m5,total,per,grade)
        cur.execute(q,val)
        conn.commit()
        print("Successfully saved")
    print("Press ENTER to continuee..")
    input()

#Delete marks entry
'''
def delete_marks_entry():
    system('color 3f')
    system('cls')
    print("DELETE STUDENT")
    print("-"*60)
    conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
    n=int(input("Enter rollno:"))
    cur=conn.cursor()
    q="select * from student where rollno=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
            print("Not Found")
    else:
        print('-'*60)
        print("Rollno        : %s"%row[0])
        print("Student name  : %s"%row[1])
        print("Father's name : %s"%row[2])
        print("Gender        : %s"%row[3])
        print("Date of birth : %s"%row[4])
        print("Address       : %s"%row[5])
        print("Phone no      : %s"%row[6])
        print("Course        : %s"%row[7])
        print("Section       : %s"%row[8])
        print('-'*60)
        ans=input('Delete it y/n?')
        if ans in 'Yy':
            conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
            cur=conn.cursor()
            q='delete from student where rollno=%s'
            val=(n,)
            cur.execute(q,val)
            conn.commit()
            print('Record has been deleted..')
            print('\nPress ENTER to continue....')
            input()
'''
#List of marks entry
            
def list_marks_entry():
    system('color 4f')
    system('cls')
    conn=mysql.connector.connect(host='localhost',user='root',database='student',password='akk@123')
    cur=conn.cursor()
    print(' '*52+"LIST OF MARKS ENTRY")
    print('-'*131)
    print("%8s %10s %10s %10s %8s %10s %8s %10s %8s %10s %8s %10s %8s "%("rno", "name", "class","sub1","marks1","sub2","marks2","sub3","marks3","sub4","marks4","sub5","marks5"))
    print('-'*131)
    q="select * from marks"
    cur.execute(q)
    for row in cur:
        print("%8s %10s %10s %10s %8s %10s %8s %10s %8s %10s %8s %10s %8s "%(row[0],row[1],row[3],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
    print('\nPress ENTER to continue....')
    input()
# Delete Marks Entry
def delete_marks_entry():
    system('color 3f')
    system('cls')
    print("DELETE MARKS ENTRY")
    print("-"*60)
    conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
    n=int(input("Enter rollno:"))
    cur=conn.cursor()
    q="select * from marks where rollno=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
            print("Not Found")
    else:
        print('-'*60)
        print("Rollno        : %s"%row[0])
        print("Student name  : %s"%row[1])
        print("Class         : %s"%row[3])
        print("Section       : %s"%row[4])
        print("%s         : %s"%(row[5],row[6]))
        print("%s           : %s"%(row[7],row[8]))
        print("%s          : %s"%(row[9],row[10]))
        print("%s           : %s"%(row[11],row[12]))
        print("%s           : %s"%(row[13],row[14]))
        print('-'*40)
        ans=input('Delete it y/n?')
        if ans in 'Yy':
            conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
            cur=conn.cursor()
            q='delete from marks where rollno=%s'
            val=(n,)
            cur.execute(q,val)
            conn.commit()
            print('Record has been deleted..')
            print('\nPress ENTER to continue....')
            input() 

def edit_marks():
    system('color 3f')
    system('cls')
    print("EDIT MARKS ENTRY")
    print("-"*60)
    conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
    n=int(input("Enter rollno:"))
    cur=conn.cursor()
    q="select * from marks where rollno=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
            print("Not Found")
    else:
        print('-'*60)
        print("Student name  : %s"%row[1])
        print("Class         : %s"%row[3])
        print("Section       : %s"%row[4])
        print("%s            : %s"%(row[5],row[6]))
        print("%s            : %s"%(row[7],row[8]))
        print("%s            : %s"%(row[9],row[10]))
        print("%s            : %s"%(row[11],row[12]))
        print("%s            : %s"%(row[13],row[14]))
        print('-'*40)
        ans=input('Edit the data y/n?')
        if ans in 'Yy':
            print('\n')
            print('Enter new data')
            print('-'*60)
            name=input("Enter the name:")
            fname=input("Enter the father name:")
            clsname=input("Enter the class:")
            section=input("Enter the section:")
            s1=input("Enter the name of first subject:")
            m1=int(input("Enter the marks of first subject:"))
            s2=input("Enter the name of  second subject:")
            m2=int(input("Enter the marks of second subject:"))
            s3=input("Enter the name of  third subject:")
            m3=int(input("Enter the marks of third subject:"))
            s4=input("Enter the name of  fourth subject:")
            m4=int(input("Enter the marks of fourth subject:"))
            s5=input("Enter the name of  fifth subject:")
            m5=int(input("Enter the marks of fifth subject:"))
            total=m1+m2+m3+m4+m5
            per=total*100/500
            if per>=80:
                grade='A'
            elif per>=60:
                grade='B'
            elif per>=40:
                grade='C'
            else:
                grade='F'
           
            conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
            cur=conn.cursor()
            q='update marks set name=%s,father_name=%s,class=%s,section=%s,subject1=%s,marks1=%s,subject2=%s,marks2=%s,subject3=%s,marks3=%s,subject4=%s,marks4=%s,subject5=%s,marks5=%s,total_marks=%s,percentage=%s,grade=%s where rollno=%s'
            val=(name,fname,clsname,section,s1,m1,s2,m2,s3,m3,s4,m4,s5,m5,total,per,grade,n)
            cur.execute(q,val)
            conn.commit()
            print("Successfully updated")
            print("Press ENTER to continuee..")
            input()

#Mark Entry Menu
    
def marks_menu():
    while True:
        system('color 9f')
        system('cls')
        print()
        print(Fore.YELLOW+Style.BRIGHT+' '*48+'MARKS ENTRY MENU')
        print(Fore.YELLOW+Style.BRIGHT+' '*44+"------------------------")
        print()
        print(Fore.RED+' '*45+'1 Marks Entry')
        print(Fore.RED+' '*45+'2 Delete Marks Record')
        print(Fore.RED+' '*45+'3 Edit Marks Entry')
        print(Fore.RED+' '*45+'4 List of Marks Entry')
        print(Fore.RED+' '*45+'5 Back To Main Menu')
        print(Fore.WHITE+' '*40+"-------------------------------------")
        print()
        print(Fore.YELLOW+Style.BRIGHT+' '*45+'Enter your choice(1-5) ?',end='')

        choice=int(input("Enrer your choice:"))    
        
        if choice==1:
            marks_entry()
        elif choice==2:
            delete_marks_entry()
        elif choice==3:
            edit_marks()
        elif choice==4:
            list_marks_entry()
        elif choice==5:
            return
        
   

    
