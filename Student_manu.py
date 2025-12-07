from student_Data_conncation import *
from varifay_Data import *
Tabel_crt()
while True:
    print("1 fro Insert Student Detals")
    print("2 for Update  ")
    print("3 for Delete ")
    print("4 search student ")
    print("5 for List Student ")
    print("6 fro Exit ")
    ch=int(input("Entert your choice "))
    if ch==1:
        name=input("ENter Name ")
        age=input("Enter Age ")
        Course=input("ENter Course ")
        Email=input("ENter Email ")
        if not validate_name(name):
            print("invalid Name")
            continue
        if not validate_age(age):
            print("invalid Age")
            continue
        if not Course_valid(Course):
            print("invalid course ")
            continue
        if not validate_Email(Email):
            print("invalid Email '@' or '.' requerd in Email ")
            continue
        Add_Student(name,int(age),Course,Email)
        print("added ")
    elif ch==2:
        s_id=input("ENter id for Update ")
        name=input("ENter Name ")
        age=input("Enter Age ")
        Course=input("ENter Course ")
        Email=input("ENter Email ")
        Update_Student(int(s_id),name,int(age),Course,Email)
        print("Updatede ")
    elif ch==3:
        s_id=input("Enter id to delete ")
        Delete_Student(s_id)
        print("Deleted ")
    elif ch==4:
        keyword=input("ENter Name/Course/Email to search ")
        result =Search_Student(keyword)
        for r in result:
            print(r)
    elif ch ==5:
        reow=Display()
        for r in reow:
            print(r)
    elif ch  ==6:
        break
    else:
        print("invalid choise ")