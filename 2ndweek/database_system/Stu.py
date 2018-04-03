#导入pymysql模块
import pymysql

#定义学生信息操作类

class stu_operate():
    #构造方法实现数据库连接
    def __init__(self):
        # 获取数据库连接
        self.db = pymysql.connect(host="localhost", user="root", password="newpass", db="test_python", charset="utf8")
        # 创建游标对象
        self.cursor = self.db.cursor()
    pass
    #查询功能
    '''
    两个参数：当前对象
    '''
    def findAll(self):
        sql = "select * from stu"
        try:
            self.cursor.execute(sql)
            print("当前学生信息:", self.cursor.rowcount)
            alist = self.cursor.fetchall()
            for single_record in alist:
                print(single_record)
        except Exception as err:
            print("sql查询执行错误!原因",err)
    #删除功能
    '''
    两个参数：对象和要删除的数据id
    '''
    def del_sth(self,num):
        sql = "delete from stu where id='%s'" % (num)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("成功删除条数：", self.cursor.rowcount)
        except Exception as err:
            self.db.rollback()
            print("sql删除执行错误!原因", err)


    #添加数据
    '''
    两个参数：对象和需要增加的数据
    '''
    def insert_sth(self,data):
        #data = (9, 'testcharm', 'hha@126.com', '2018-3-28 14:23:34')
        sql = "insert into stu(id,name,sex,classid)values('%d','%s','%s','%s')" % (data)
        try:
            self.cursor.execute(sql)

            # 事物提交，才能在数据库看到你新加入的数据
            self.db.commit()
            print("成功添加条数：", self.cursor.rowcount)
        except Exception as err:
            self.db.rollback()
            print("sql增加错误!原因", err)


    #析构方法关闭数据库连接
    def __del__(self):
        self.db.close()
    pass
