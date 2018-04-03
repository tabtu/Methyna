#导入pymysql模块
import pymysql
from database_system import Stu


while True:
    print("="*12,"学员管理系统","="*12)
    print("{0:1}{1:13}{2:15}".format(" ","1.查看学员信息","2.添加学员信息"))
    print("{0:1}{1:13}{2:15}".format(" ","3.删除学员信息","4.退出系统"))
    print("="*36)
    key = input("请输入对应的选择：")
    student_operation = Stu.stu_operate()

    if key == '1':
        print("=" * 12, "学员信息浏览", "=" * 14)
        student_operation.findAll()
        input("按回车继续...")

    elif key == '2':
        print("=" * 12, "学员信息添加", "=" * 14)

        new_id= int(input("请输入要添加的id："))
        new_name = input("请输入要添加的名字：")
        new_sex = input("请输入要添加的性别：")
        new_classid = input("请输入要添加的班级：")
        new_stu = (new_id,new_name,new_sex,new_classid)
       # new_stu = " ".join(list(new_stu))
        student_operation.insert_sth(new_stu)
        input("按回车继续...")
    elif key == '3':
        print("=" * 12, "学员信息删除", "=" * 14)
        sid = input("请输入你要删除的信息id号：")
        student_operation.del_sth(sid)
        input("按回车继续...")
    elif key == '4':
        print("=" * 12, "再见", "=" * 14)
        break
    else:
        print("=======无效的键盘输入=======")
