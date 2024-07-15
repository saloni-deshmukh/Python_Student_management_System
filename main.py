

from insert import insertdata
from update import updatedata
from delete import deletedata
from read import readdata

obj = insertdata()

print("-------STUDENT MANAGEMENT SYSTEM-------")
print("For Insertion press 1, Updation press 2 \n Deletion press 3, Reading press 4")

num = int(input("Please enter your options : "))

if num == 1 :
    print("Choose 1 for student:\nChoose 2 for course:\nChoose 3 for transaction\n")
    n = int(input("Please enter your option : "))

    if n == 1 :
        sid = int(input("Enter your ID : "))
        sname = input("Enter your name : ")
        email = input("Enter your mail : ")
        city = input("Enter your city : ")
        obj.insertstudent(sid,sname,email,city)

    if n == 2 :               
        course = int(input("Enter course id : "))
        coursename = input("Enter the course name : ")
        sid = int(input("Enter the student ID: "))
        price = float(input("Enter the price of the course: "))
        obj.insertcourse(course, coursename, sid, price)

    if n == 3 :               
        tid = int(input("Enter transaction id : "))
        sid = int(input("Enter the student ID : "))
        course = int(input("Enter the course ID : "))
        method = input("Enter the method of transaction : ")
        obj.inserttransaction(tid, sid, course, method)



obj2 = updatedata()

if num == 2 :
    print("Choose 1 to update student name : \n Choose 2 to update course : \n Choose 3 to update transaction details \n")
    n = int(input("Please enter your option : "))

    if n==1:
        inpid = int(input("Enter your ID : "))
        sid = int(input("Enter your updated ID : "))
        sname = input("Enter your updated name : ")
        email = input("Enter your updated mail : ")
        city = input("Enter your updated city : ")
        obj2.updatestudent(inpid,sid,sname,email,city)

    if n==2 :
        inpid = int(input("Enter your ID : "))
        course = int(input("Enter your updated course id : "))
        coursename = input("Enter your updated course name : ")
        price = float(input("Enter the price of the updated course: "))
        obj2.updatecourse(inpid,course,coursename,price)

    if n==3 :
        inpid = int(input("Enter your ID : ")) 
        tid = int(input("Update your TID : "))
        course = int(input("Enter your course : "))
        method = input("Update the method of transaction : ")
        obj2.updatetrans(inpid,tid,course,method)



obj3 = deletedata()

if num == 3 :
    print("Choose 1 to delete student name : \n Choose 2 to delete course : \n Choose 3 to delete transaction details \n")
    n = int(input("Please enter your option : "))

    if n==1:
        sid = int(input("Enter your ID : "))
        obj3.deletestudent(sid)


obj4 = readdata()

if num == 4 :
    
    sid = int(input("Enter your ID : "))
    obj4.readstudent(sid)







    

