# 完成一轮排序过程
def sub_sort(list,low,high):
  #　基准数
  x = list[low]
  while low < high:
    #　后面的数小于ｘ放到前面的空位
    while list[high] >= x and high > low:
      high -= 1
    list[low] = list[high] #　将数往前甩
    while list[low] < x and low < high:
      low += 1
    list[high] = list[low]
  list[low] = x #　将基准数插入
  return low

#　快排 low 第一个数序列号　high 最后一个数序列号
def quick(list,low,high):
  if low < high:
    key = sub_sort(list,low,high)
    quick(list,low,key - 1)
    quick(list, key+1, high)

l = [3,7,6,5,8,3,4,2]
quick(l,0,7)
print(l)


""" 
day22     
数据结构
  1. 数据结构的理论概念
  2. 线性结构的实现 (链表,栈,队列)
  3. 认识树状模型,二叉树的遍历
  4. 了解的基本查找排序行为
"""





