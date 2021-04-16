# coding=utf-8
def QuickSort(list, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = list[i]

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (list[j] >= base):
                j = j - 1

            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            list[i] = list[j]

            # 同样的方式比较前半区
            while (i < j) and (list[i] <= base):
                i = i + 1
            list[j] = list[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        list[i] = base

        # 递归前后半区
        QuickSort(list, start, i - 1)
        QuickSort(list, j + 1, end)
    return list


list = [3, 9, 1, 2, 5, 7, 4, 8, 6]
QuickSort(list, 0, len(list) - 1)
print(list)
