"""
1 .二维数组的查找
题目描述
在一个二维数组中（每个一维数组的长度相同）
每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

理解
什么是二维数组？
实际上python当中没有数组的概念, 而是列表(List), 二维列表相当于二维数组 。

解题思路
思路1：
直接循环遍历每一个元素，判断是否等于给定的整数，如果相等则输出存在，否则不存在
"""""
class Soluton:
	def Find(self,target,array):
        #array是二维列表
		for i in range(len(array)):
			for j in range(len(array[0])):
				if array[i][j]==target:
					return True
		return False
"""
思路2：
由于数组元素是分别按行按列递增的，故可以：
从最后一行第一列开始遍历
记给定的整数为target，数组元素为array[i][j]
如果 target < array[i][j] 则行数减1
如果 target > array[i][j] 则列数加1
如果 target == array[i][j] 则返还True
"""
class Solution:
    def Find(self,target,array):
        #array为二维列表
        rows=len(array)-1
        cols=len(array[0])-1
        i=rows
        j=0
        while i >=0 and j<=cols:
            if target<array[i][j]:
                i-=1
            elif target>array[i][j]:
                j+=1
            else:
                return True
        return False