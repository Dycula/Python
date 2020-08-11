"""
业务逻辑模块bll
"""

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
