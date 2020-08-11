""""""

"""
项目三：２０４８ 游戏
规则
    1. 游戏运行，在４＊４的方格中，出现两个随机的数字．
    	-- 产生随机数的策略：10%的概率是４，90%的概率是2.
    2. 用户移动方格（wsad）,方格内的数字按照相应规则进行合并．
    3. 如果地图有变化(数字移动／数字合并)，再产生１个随机数．
    4. 游戏结束：数字不能合并，也没有空白位置．
架构
    逻辑处理模块 Controller
    界面视图模块 View
    数据模型模块 Model                                    
    程序入口模块 Main
步骤
    （一）逻辑处理模块 
       创建游戏核心类GameCoreController
       (1)将核心算法粘贴进来
       (2)将所有参数，改为成员变量。
       (3)产生新数字
       　　　-- 计算所有空白位置(为０的位置).
             -- 随机选择一个位置
             -- 根据概率产生数字，存入列表的相应位置．
   （二）界面视图模块
   　　　创建游戏核心类对象
   　　　调用核心类对象的生成数字方法
      　　while True:
            呈现界面
            获取用户输入，调用核心类对象的移动方法．　
            产生随机数
  　(三)如果地图有变化(数字移动／数字合并)，再产生１个随机数．
  　(四)游戏结束：数字不能合并，也没有空白位置．
"""
class Location:
    """
        位置类
    """

    def __init__(self, r, c):
        self.r_index = r
        self.c_index = c

    @property
    def r_index(self):
        return self.__r_index

    @r_index.setter
    def r_index(self, value):
        self.__r_index = value

    @property
    def c_index(self):
        return self.__c_index

    @c_index.setter
    def c_index(self, value):
        self.__c_index = value


class Direction:
    """
        方向
    """
    up = 0
    down = 1
    left = 2
    right = 3


import random
import copy
class GameCoreController:
    """
        游戏核心控制器
    """

    def __init__(self):
        # self.__map = [
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        # ]
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4,
        ]
        # 以下数据，是为了测试地图是否发生变化创建的．
        # self.__map = [
        #     [2, 4, 2, 4],
        #     [0, 0, 0, 2],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 0],
        # ]
        # 以下数据，是为了测试游戏是否结束创建的．
        # self.__map = [
        #     [2, 4, 2, 4],
        #     [8, 16, 4, 32],
        #     [32, 4, 2, 64],
        #     [64, 32, 16, 0],
        # ]
        # 用于存储去零和合并的列表
        self.__list_merge = []
        # 用于存储空位置的列表
        self.__list_empty_location = []
        # 地图是否发生变化
        self.is_change = False

    @property
    def map(self):
        return self.__map

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.__list_merge[i + 1] = 0
        self.__zero_to_end()

    def __move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r]
            self.__merge()
            self.__map[r][:] = self.__list_merge

    def __move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r][::-1]
            self.__merge()
            self.__map[r][::-1] = self.__list_merge

    def __move_up(self):
        for c in range(4):
            # 清空合并列表，目的：避免之前列表中的结果，对本次有影响．
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(self.__map[r][c])
            self.__merge()
            for r in range(4):
                self.__map[r][c] = self.__list_merge[r]

    def __move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):
                self.__list_merge.append(self.__map[r][c])
            self.__merge()
            for r in range(3, -1, -1):
                self.__map[r][c] = self.__list_merge[3 - r]

    def move(self, dir):
        """
            移动
        :param dir: Direction类型　
        :return:
        """
        # 通过深拷贝(二维列表)记录移动前的地图　
        original_map = copy.deepcopy(self.__map)

        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()

        # 移动后对比地图
        self.is_change = original_map != self.__map

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(4):
            for c in range(4):
                if self.__map[r][c] == 0:
                    # 创建位置对象
                    loc = Location(r, c)
                    self.__list_empty_location.append(loc)

    def generate_new_number(self):
        """
            随机生成新数字
        :return:
        """
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        # 从空位置列表中，随机选择一个元素．
        loc = random.choice(self.__list_empty_location)
        # 随机生成数字
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        # 因为上一行代码已经占了该空位置，所以从空位置列表中移除当前位置．
        self.__list_empty_location.remove(loc)

    def is_game_over(self):
        """
            游戏是否结束
        :return:
        """
        # 1. 如果有空位置 游戏不能结束
        if len(self.__list_empty_location) >0:
            return False

        # # 2. 横向具有相同元素　游戏不能结束
        # for r in range(4):
        #     for c in range(3):
        #         if self.__map[r][c] == self.__map[r][c+1]:
        #             return False
        #
        # # 3. 竖向具有相同元素　游戏不能结束
        # for c in range(4):
        #     for r in range(3):
        #         if self.__map[r][c] == self.__map[r+1][c]:
        #             return False

        # (扩展)　2 + 3  横向同时竖向　比较是否具有相同元素
        for r in range(4):
            for c in range(3):
                if self.__map[r][c] == self.__map[r][c+1] or self.__map[c][r] == self.__map[c+1][r]:
                    return False

        return True # 如果以上条件都不满足，则游戏结束

import os
class GameConsoleView:
    """
        控制台视图
    """

    def __init__(self):
        # 　创建核心类对象
        self.__controller = GameCoreController()

    def start(self):
        """
            游戏开始
        """
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        # 清空控制台
        os.system("clear")
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c], end="\t")
            print()

    def update(self):
        """
            更新(游戏逻辑)
        :return:
        """
        while True:
            self.__move_map()
            # if 界面发生变化
            if self.__controller.is_change:
                self.__controller.generate_new_number()
                self.__print_map()
                if self.__controller.is_game_over():
                    print("游戏结束")
                    break

    def __move_map(self):
        dir = input("请输入移动方向(wsad)")
        if dir == "w":
            self.__controller.move(Direction.up)
        elif dir == "s":
            self.__controller.move(Direction.down)
        elif dir == "a":
            self.__controller.move(Direction.left)
        elif dir == "d":
            self.__controller.move(Direction.right)

if __name__ == "__main__":
    view = GameConsoleView()
    view.start()
    view.update()