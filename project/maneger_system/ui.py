"""
程序界面模块 ui
"""
from bll import *
from model import  *

class StudentManagerView:
    """
      学生管理器视图
    """

    def __init__(self):
        # 创建控制器对象
        self.__manager = StudentManagerController()

    def __display_menu(self):
        """
        显示菜单
        :return:
        """
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩升序显示")

    def __select_menu_item(self):
        """
          选择菜单项
        :return:
        """
        number = input("请输入选项:")
        if number == "1":
            # 执行添加学生逻辑
            self.__input_student()
        elif number == "2":
            self.__output_students(self.__manager.stu_list)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()

    def main(self):
        """
          入口逻辑
        """
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_student(self):
        """
          输入学生
        """
        name = input("请输入姓名:")
        age = int(input("请输入年龄:"))
        score = int(input("请输入成绩:"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self, list_stu):
        """
          显示所有学生
        """
        for item in list_stu:
            print("%d---%s---%d---%d" % (item.id, item.name, item.age, item.score))

    def __delete_student(self,list_stu):
        '''
        删除学生
        '''
        id=int(input("请输入需要删除的学生编号:"))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        '''
        修改学生信息
        '''
        stu = StudentModel()
        stu.id = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入姓名:")
        stu.age = int(input("请输入年龄:"))
        stu.score = int(input("请输入成绩:"))
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")