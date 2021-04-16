# coding=utf-8
def sort(list):
    length = len(list)
    start = 0
    end = length - 1

    while start < end:
        # 正序
        flage = False
        # 先让初始的两个有序
        if list[start] > list[start + 1]:
            list[start], list[start + 1] = list[start + 1], list[start]

        for i in range(start + 1, end):
            # 一次找两个最大的元素，为什么是两个，因为不用第二次比较，假如比这两个中的第一个大就让第一个向后挪，如果比第一个小，就和第二个比较
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                flage = True
                if list[i] < list[i - 1]:
                    list[i], list[i - 1] = list[i - 1], list[i]

        end -= 2
        if list[end] < list[end - 1]:
            list[end], list[end - 1] = list[end - 1], list[end]

        for j in range(end - 1, start, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                flage = True
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        start += 2
        if not flage:
            break
    return list


result = sort([8, 6, 4, 3, 9, 1, 2, 5, 7])
print(result)
