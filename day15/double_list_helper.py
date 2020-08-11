"""
  二维列表助手
    用于定义对二维列表的常用操作.
"""


class Vector2:
  """
    向量
  """

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @staticmethod
  def get_right():
    return Vector2(0, 1)

  @staticmethod
  def get_up():
    return Vector2(-1, 0)

  @staticmethod
  def get_left():
    return Vector2(0, -1)

  @staticmethod
  def get_down():
    return Vector2(1, 0)


def get_elements(target, vect_pos, vect_dir, count):
  """
    获取二维列表中,某个位置,某个方向,指定数量的元素.
  :param target:
  :param vect_pos:
  :param vect_dir:
  :param count:
  :return:
  """
  result = []
  for i in range(count):
    # 改变位置:原位置 + 方向
    vect_pos.x += vect_dir.x
    vect_pos.y += vect_dir.y
    result.append(target[vect_pos.x][vect_pos.y])
  return result

# 当前模块被导入时,测试代码也会执行.
print("ok")

# 目的:测试代码不要在导入当前模块时执行.
if __name__ == "__main__":
  list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
  ]
  pos = Vector2(1, 0)
  dir = Vector2.get_right()  # 0 1
  re = get_elements(list01, pos, dir, 2)
  print(re)









