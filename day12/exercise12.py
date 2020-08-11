#day12作业
#1.三合一
#2.独立完成当天练习
#3.根据文档,逐步实现:project_month01／manager_system.text
#4.实现删除/修改功能/按照成绩升序显示功能
#5.尝试将面向过程的购物车改写为面向对象的购物车,
#  体会面向过程与面向对象的不同设计思想

# 数据模型类：StudentModel
#		数据：编号 id,姓名 name,年龄 age,成绩 score
class StudentModel:
    '''
    学生数据模型
    '''

    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, vaule):
        self.__id = vaule

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, vaule):
        self.__name = vaule

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, vaule):
        self.__age = vaule

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, vaule):
        self.__score = vaule


# 1.产品经理：将用户的需求,写成产品规格说明文档
# 2.程序员：需求分析-->架构设计(概要设计/详细设计)-->编码-->单元测试
# 3.测试员:自动化测试
# 4.上线维护

# 逻辑控制类：StudentManagerController
#		数据：学生列表 __stu_list
#		行为：获取列表 stu_list,添加学生 add_student
#		删除学生remove_student，修改学生update_student
#		根据成绩排序order_by_score。
class StudentManagerController:
    """
      逻辑控制类
    """

    def __init__(self):
        # 数据结果:[StudentModel(...),StudentModel(...)]
        self.__stu_list = []

    @property
    def stu_list(self):
        # 缺点列表地址,外部还能修改列表元素
        return self.__stu_list
        # 缺点:每次返回新的列表(赋值一个新的列表),占用内存
        # return self.__stu_list[:]

    def add_student(self, new_stu):
        """
          添加学生
        :param new_stu: 没有id的新学生
        """
        new_stu.id = self.__generate_id()
        self.__stu_list.append(new_stu)

    def __generate_id(self):
        # 最后一个学生编号+1
        return self.__stu_list[-1].id + 1 if len(self.__stu_list) > 0 else 1

    def remove_student(self, id):
        '''
        删除学生
        :param id: 学生编号
        :return: 是否返回成功
        '''
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
            return False

    def update_student(self, stu_info):
        '''
        根据编号修改其余信息
        :param stu_info: 学生信息
        :return: 是否修改成功
        '''
        for item in self.__stu_list:
            if item.id == stu_info.id:
                # 修改学生对象
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False


# controller = StudentManagerController()
# controller.add_student(StudentModel("无极",25,100))
# controller.add_student(StudentModel("无极",25,100))
# 测试添加学生
# for item in controller.stu_list:
#   print(item.id)
# 测试删除学生
# re=controller.remove_student(1)
# for item in controller.stu_list:　
#    print(item.id)
# 测试修改学生
# stu=StudentModel("赵敏",23,90,2)
# controller.update_student(stu)
# for item in controller.stu_list:
#    print(item.name)

# 界面视图类：StudentManagerView
# 行为：显示菜单__display_menu，
# 选择菜单项__select_menu_item，
# 入口逻辑main
# 输入学生__input_students，
# 输出学生__output_students，
# 删除学生__delete_student，
# 修改学生信息__modify_student，
# 按成绩输出学生__output_student_by_score
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


view = StudentManagerView()
view.main()




