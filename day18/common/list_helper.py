class ListHelper:
  """
    列表助手:定义列表的常用操作.
  """

  @staticmethod
  def find(list_target, func_condition):
    """
      在列表中根据指定条件查找所有元素.
    :param list_target: 目标列表
    :param func_condition: 查找条件
    :return: 生成器对象
    """
    for item in list_target:
      if func_condition(item):
        yield item

  @staticmethod
  def first(list_target, func_condition):
    """
        在列表中查找第一个满足条件的元素.
      :param list_target: 目标列表
      :param func_condition: 查找条件
      :return: 满足条件的第一个元素
    """
    for item in list_target:
      if func_condition(item):
        return item

  @staticmethod
  def get_count(list_target, func_condition):
    """
      获取满足条件的元素数量
    :param list_target: 目标列表
    :param func_condition: 查找条件
    :return: 数量
    """
    count_value = 0
    for item in list_target:
      if func_condition(item):
        count_value += 1
    return count_value

  @staticmethod
  def sum(list_target, func_handle):
    """
      自定义类的列表求和
    :param list_target: 目标列表
    :param func_handle: 元素(自定义类)的处理逻辑
    :return: 总和
    """
    sum_value = 0
    for item in list_target:
      sum_value += func_handle(item)
    return sum_value

  @staticmethod
  def get_max(list_target, func_condition):
    """
      在列表中获取满足条件的最大元素
    :param list_target: 目标列表
    :param func_condition: 条件
    :return: 最大的元素
    """
    max = list_target[0]
    for i in range(1, len(list_target)):
      # if max.atk  <  list_target[i].atk:
      # if max.speed  <  list_target[i].speed:
      if func_condition(max) < func_condition(list_target[i]):
        max = list_target[i]
    return max

  @staticmethod
  def select(list_target, func_condition):
    """
      根据条件,筛选列表.
    :param list_target: 目标列表
    :param func_condition: 条件
    :return: 需要的数据所组成的列表
    """
    result = []
    for item in list_target:
      # result.append(item.name)
      result.append(func_condition(item))
    return result

  @staticmethod
  def order_by(list_target,func_condition):
    """
      根据条件对列表进行升序排列
    :param list_target: 目标列表
    :param func_condition: 排序条件
    """
    for r in range(len(list_target) - 1):
      for c in range(r + 1, len(list_target)):
        # if list_target[r].atk > list_target[c].atk:
        if func_condition(list_target[r]) > func_condition(list_target[c]):
          list_target[r], list_target[c] = list_target[c], list_target[r]






