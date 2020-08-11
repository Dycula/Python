#day13
#1.三合一
#2.当天练习独立完成
#3.开放性作业:洞察客观世界的事物,自行定义子类(2个)与父类(1个)
class Employee:
    """
      #员工
    """

    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def employee_money(self):
        return self.basic_salary

class Programmer(Employee):
    def __init__(self, project_commission, basic_salary):
        super().__init__(basic_salary)
        self.project_commission = project_commission

class Saleman(Employee):
    def __init__(self, commission, basic_salary):
        super().__init__(basic_salary)
        self.commission = commission
#4.(扩展)有若干个图形(圆形/矩形...)
#定义图形管理器,记录所有图形(多个圆形对象,多个矩形对象)
#提供计算总面积的方法
# --------------调用者--------------------
class GraphicManager:
  """
    #图形管理器
  """

  def __init__(self):
    self.__graphics = []

  def add_graphic(self, graphic):
    self.__graphics.append(graphic)

  def get_total_area(self):
    total_area = 0
    for item in self.__graphics:
      # 希望调用的是父类方法(一种动作)
      # 实际执行的是子类方法(不同实现方式)
      # 体现了多态性.
      total_area += item.calculate_area()
    return total_area


class Graphic:
  """
    #图形
  """

  def calculate_area(self):
    pass


# -----------------定义者---------------------
class Circle(Graphic):
  """
    圆形
  """

  def __init__(self, r):
    self.radius = r

  def calculate_area(self):
    return 3.14 * self.radius ** 2


class Rectangle(Graphic):
  def __init__(self, l, w):
    self.length = l
    self.width = w

  def calculate_area(self):
    return self.length * self.width


# ----------测试-------------
manager = GraphicManager()
g01 = Circle(10)
manager.add_graphic(g01)
manager.add_graphic(Rectangle(10, 20))
result = manager.get_total_area()
print(result)
#5.穷尽一切手段在互联网上搜集继承与多态相关的资料,并结合课堂所讲,写成自述文档
#关键词:继承,多态,面向对象,三大特征,开闭原则,依赖倒置


#python里面的如何拷贝一个对象？(赋值,浅拷贝,深拷贝的区别)
#赋值：创建一个变量或改变一个变量绑定的数据
#浅拷贝：是在复制过程中,只复制一层变量,不会复制深层变量绑定的对象的复制过程。
#深拷贝：复制整个依懒的变量。
#单引号,双引号,三引号的区别？
#三种引号都可以表示字符串
#在字符串中单引和双引号的区别
#  1. 单引号内的双引号不算结束符
#  2. 双引号内的单引号不算结束符
#三引号作用
#  1. 换行会自动转换为换行符\n
#  2. 三引号内可以包含单引号和双引号
#  3. 作为文档字符串
#下面代码会输出什么：
#def f(x,l=[]):
#    for i in range(x):
#        l.append(i*i)
#    print(l)
#f(2)#[0,1]
#f(3,[3,2,1])#[3,2,1,0,1,4]
#f(3)#[0,1,4]
#什么是匿名函数？匿名函数有什么局限性？
#没有名称的函数,由编译器指定名称并分配空间,通常直接作为参数传递
#匿名函数不以文件的形式主流在文件夹上,可在指令窗或任何函数体内通过指令直接生成
#匿名函数的局限性:只能有一个表达式,不用写return,返回值就是该表达式的结果
#思考题：变态台阶问题
#一只青蛙一次可以跳1级台阶,也可以跳2级.....他也可以跳n级.
#求该青蛙跳上一个n级的台阶总共有多少种跳法   2^(n-1)
#1
#1+1  2
#3  1+1+1 1+2 2+1#
#4  1+1+1+1 1+3 1+1+2 1+2+1 2+2 3+1 2+1+1 4

def fun(n):
    if n==0:
        return 0
    else:
        return 2**(n-1)
result=fun(3)
print(result)

