from colorama import *
from os import *
import mysql.connector

#ADD NEW STUDENT
def add_student():
    system('color 5f')
    system('cls')
    print("ADD NEW STUDENT")
    print("-"*60)
    rno=int(input("Enter the rollno   : "))
    name=input("Enter student name   :")
    fname=input("Enter father's name  :")
    gender=input("Enter the gender m/f  :")
    print("Enter date of birth  :")
    d=int(input('Day  :'))
    m=int(input('Month:'))
    y=int(input('Year:'))
    address=input("Enter the address  :")
    phno=int(input("Enter the phoneno  :"))
    course=input("Enter the course :")
    section=input("Enter the section  :")
    dob=str(y)+'-'+str(m)+'-'+str(d)
    conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
    cur=conn.cursor()


    q="insert into student (rollno ,name ,fname ,gender, dob ,address ,phone ,course,section) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(rno,name,fname,gender,dob,address,phno,course,section)
    
    cur.execute(q,val)
    conn.commit()
    print('\n Successfully saved')
    print('\nPress ENTER to continue....')
    input()

    
def delete_student():
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


def list_students():
    system('color 4f')
    system('cls')
    conn=mysql.connector.connect(host='localhost',user='root',database='student',password='akk@123')
    cur=conn.cursor()
    print(' '*52+"LIST OF STUDENTS")
    print('-'*131)
    print("%8s %15s %15s %15s %10s %15s %15s %15s %10s"%("rno","name","fname","gender","dob","address","phno","course","section"))
    print('-'*131)
    q="select * from student"
    cur.execute(q)
    for row in cur:
        print("%8s %15s %15s %10s %15s %15s %15s %15s %8s"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    print('\nPress ENTER to continue....')
    input()
def search_by_rollno():
    system('color 4f')
    system('cls')
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
        print('\nPress ENTER to continue....')
        input()

def search_by_name():
    system('color 9f')
    system('cls')
    n=input("Enter name:")
    conn=mysql.connector.connect(host='localhost',user='root',database='student',password='akk@123')
    cur=conn.cursor()
    print(' '*52+"LIST OF STUDENTS")
    print('-'*131)
    print("%8s %15s %15s %15s %10s %15s %15s %15s %10s"%("rno","name","fname","gender","dob","address","phno","course","section"))
    print('-'*131)
    q="select * from student where name=%s"
    val=(n,)
    cur.execute(q,val)
    for row in cur:
        print("%8s %15s %15s %10s %15s %15s %15s %15s %8s"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    print('\nPress ENTER to continue....')
    input()

def search_by_course():
    system('color 9f')
    system('cls')
    n=input("Enter course:")
    conn=mysql.connector.connect(host='localhost',user='root',database='student',password='akk@123')
    cur=conn.cursor()
    print(' '*52+"LIST OF STUDENTS")
    print('-'*131)
    print("%8s %15s %15s %15s %10s %15s %15s %15s %10s"%("rno","name","fname","gender","dob","address","phno","course","section"))
    print('-'*131)
    q="select * from student where course=%s"
    val=(n,)
    cur.execute(q,val)
    for row in cur:
        print("%8s %15s %15s %10s %15s %15s %15s %15s %8s"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    print('\nPress ENTER to continue....')
    input()

    
#Search menu
    
def search_menu():
    while True:
        system('color 4f')
        system('cls')
        print(Fore.YELLOW+Style.BRIGHT+"SEARCH MENU")
        print('-----------------------------')
        print('1  Search by rollno')
        print('2  Search by name')
        print('3  Search by course')
        print('4  Back to student menu')
        print("-----------------------------")
        choice=int(input("Enter your choice ? "))
        if choice==1:
            search_by_rollno()
        elif choice==2:
            search_by_name()
        elif choice==3:
            search_by_course()
        elif choice==4:
            return()
        



    
def student_menu():
    while True:
        system('color 3f')
        system('cls')
        print()
        print(Fore.BLUE+' '*48+"STUDENT MENU ")
        print(Fore.BLUE+' '*44+"------------------------")
        print()
        print(Fore.RED+' '*45+'1 Add New Student')
        print(Fore.RED+' '*45+'2 Delete Student Record')
        print(Fore.RED+' '*45+'3 Search Student')
        print(Fore.RED+' '*45+'4 List For Students')
        print(Fore.RED+' '*45+'5 Back To Main Menu')
        print(Fore.BLUE+' '*40+"-------------------------------------")
        print()
        print(Fore.BLUE+' '*45+'Enter your choice(1-5) ?',end='')
        choice=int(input())
        if choice==1:
            add_student()
        elif choice==2:
            delete_student()
        elif choice==3:
            search_menu()
        elif choice==4:
            list_students()
        elif choice==5:
            return
    
        
