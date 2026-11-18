from colorama import *
from pwinput import *
from os import *
from tqdm import *
import time
import mysql.connector
import student_lib
import marks_lib

system('color 4f')
system('cls')
print('\n'*15)
p=pwinput(Fore.WHITE+Style.BRIGHT+' '*55+"Enter password : ",mask="*")
conn=mysql.connector.connect(host='localhost',user='root',database='student',password='akk@123')
cur=conn.cursor()
q="select * from admin where binary password=%s"
val=(p,)
cur.execute(q,val)
row=cur.fetchone()
if(row==None):
    print()
    print(Fore.YELLOW+' '*55+"Incorrect Password")
    print()
    print(' '*55+'Press ENTER to continue....')
    input()
    sys.exit()
else:
    
    system('color 9f')
    system('cls')

    
    print('\n'*4)
    print(Fore.YELLOW+' '*45+"S T U D E N T  M A N A G E M E N T")
    print()
    print(' '*45 +"                &")
    print()
    print(' '*32+"G E N E R A T E  R E P O R T  C A R D  /  M A R K S H E E T")
    print("\n"*3)
    print(Fore.GREEN+' '*55+"Version:1.0")
    print("\n"*4)
    print(Fore.RED+' '*55+"Developed By:")
    print(Fore.BLUE+' '*53+' '*2+"Akshansh And Akshit")
    print()
    print()
    for i in tqdm(range(40),desc="Please wait"):
        time.sleep(0.1)
def change_password():
    system('color 4f')
    system('cls')
    new_pass=input("Enter new password:")
    confirm_pass=input('Confirm password:')
    
    if(new_pass!=confirm_pass):
        print("\nPassword not Match")
        print('\nPress ENTER to continue....')
        input()
        sys.exit()
    else:
        conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
        cur=conn.cursor()
        q="update admin set password=%s";
        val=(new_pass,)
        cur.execute(q,val)
        conn.commit()
        print("Successfully updated")
def report_card_menu():
    system('color 4f')
    system('cls')
    print("Display REPORT CARD")
    print("-"*60)
    conn=mysql.connector.connect(host='localhost',user='root',password='akk@123',database='student')
    n=int(input("Enter rollno:"))
    cur=conn.cursor()
    #q="select marks.rollno,student.rollno,marks.name,marks.father_name,student.dob,marks.class,marks.section from marks,student where student.rollno=marks.rollno and marks.rollno=%s"
    q="select * from marks where rollno=%s"
    val=(n,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print("Not Found")
        print("Press ENTER to continuee..")
        input()
    else:
        print()
        system('color 5f')
        system('cls' )
        print("                                         Meerut Institute Of Engineering And Technology")
        print("                                         "+'-'*47)
        print("                                                          NH 58, MERRUT")
        print("                                                          "+'-'*13)
        print()
        print("                                                        M A R K S H E E T")
        print("                                                        "+'-'*17)
        print()
        print("Roll Number  : %s"%row[0])
        print("Course/Class : %s"%row[4])
        print("Student Name : %s"%row[1])
        print("Section      : %s"%row[5])
        print("Father's Name: %s"%row[2])
        print("Date Of Birth: %s"%row[3])
        print()
        q="select * from marks where rollno=%s"
        val=(n,)
        cur.execute(q,val)
        row=cur.fetchone()
        if row[6]>=80:
            g1='A'
        elif row[6]>=60:
            g1='B'
        elif row[6]>=40:
            g1='C'
        else:
            g1='F'

        if row[8]>=80:
            g1='A'
        elif row[8]>=60:
            g1='B'
        elif row[8]>=40:
            g1='C'
        else:
            g1='F'

        if row[10]>=80:
            g1='A'
        elif row[10]>=60:
            g1='B'
        elif row[10]>=40:
            g1='C'
        else:
            g1='F'

        if row[12]>=80:
            g1='A'
        elif row[12]>=60:
            g1='B'
        elif row[12]>=40:
            g1='C'
        else:
            g1='F'

        if row[14]>=80:
            g1='A'
        elif row[14]>=60:
            g1='B'
        elif row[14]>=40:
            g1='C'
        else:
            g1='F'
            
        
        print('-'*130)
        print("%20s%30s%30s%25s"%("SUBJECT NAME","MAX MARKS","OBTAINED MARKS","GRADE"))
        print('-'*130)
        print("%20s%30s%30s%25s"%(row[5],100,row[6],g1))
        
        print("%20s%30s%30s%25s"%(row[7],100,row[8],g1))

        print("%20s%30s%30s%25s"%(row[9],100,row[10],g1))
    
        print("%20s%30s%30s%25s"%(row[11],100,row[12],g1))

        print("%20s%30s%30s%25s"%(row[13],100,row[14],g1))
        print('-'*130)
        print()
        print(" "*55+"Total_Marks:",row[15])
        print()
        print(" "*55+"Percentage:",row[16])
        print()
        print("Press ENTER to continuee..")
        input()
    

while True:
    system('color 6f')
    system('cls')
    print()
    print(Fore.BLUE+' '*47+" M A I N  M E N U ")
    print(Fore.BLUE+' '*44+"------------------------")
    print()
    print(Fore.RED+' '*45+'1 STUDENT MENU')
    print()
    print(Fore.RED+' '*45+'2 MARKS ENTRY  MENU')
    print()
    print(Fore.RED+' '*45+'3 REPORT CARD MARKSHEET')
    print()
    print(Fore.RED+' '*45+'4 CHANGE PASSWORD')
    print()
    print(Fore.RED+' '*45+'5 EXIT')
    print()
    print(Fore.BLUE+' '*40+"-------------------------------------")

    print()
    print(Fore.BLUE+' '*45+'Enter your choice(1-5) ?',end='')
    choice=int(input())
    if choice==1:
        student_lib.student_menu()
    elif choice==2:
        marks_lib.marks_menu()
    elif choice==3:
        report_card_menu()
    elif choice==4:
        change_password()
    elif choice==5:
        import sys
        sys.exit()
    
        

