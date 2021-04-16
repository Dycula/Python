# coding=utf-8
list = [66, 77, 99, 33, 44, 88, 22, 11, 55]
list.sort()
n = len(list)


def fun(list, key, start, end):
    if list[0] <= key <= list[-1]:
        mid = (start + end) // 2
        if list[mid] == key:
            return mid
        if start > end:
            return "xxx"
        elif list[mid] < key:
            return fun(list, key, mid + 1, end)
        else:
            return fun(list, key, start, mid - 1)
    else:
        return "xxx"


result = fun(list, 44, 0, 8)
print(result)
