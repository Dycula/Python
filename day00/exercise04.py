"""
重建二叉树
题目描述：输入某二叉树的前序遍历和中序遍历的结果,请重建出该二叉树
假设输入的前序遍历和中序遍历的结果中都不含重复的数字.
例如输入前序遍历序列为{1,2,4,7,3,5,6,8}和中序遍历序列为{4,7,2,1,5,3,8,6},
则重建二叉树并返回。
"""
class TreeNode:
    def __inint__(self,x):
        self.val=x
        self.left=None
        self.right=None
"""
二叉树的遍历（参考：二叉树遍历，重建二叉树）
前序遍历（NLR）
遍历顺序为（根-左-右），每次读取的第一个值一定是根节点，这样我们可以在中序遍历的序列中找到当前的根节点的位置。
中序遍历（ LNR）
遍历顺序为（左-根-右），当确定了一个根节点后，其左边序列就是这个根节点的左子树，右边序列就是其右子树。
后序遍历（ LRN）
遍历顺序为（左-右-根）
可以发现N的位置决定二叉树的遍历方式。
二叉树的每个节点最多有两颗子树。
已知前序遍历和中序遍历 或 已知中序遍历和后序遍历，均可确定一颗二叉树，但已知前序遍历和后序遍历不能确定一颗二叉树。
"""
class Solution:
    # 返回构造的TreeNode根节点
    # 根据前序遍历和中序遍历重建二叉树
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        # 遇到树的问题优先考虑使用递归
        # pre为前序遍历，tin为中序遍历
        if not pre or not tin:
            return None
        # 前序遍历的第一个值为根节点
        root = TreeNode(pre[0])
        # 在中序遍历中找到根节点,也是中心位置
        val = tin.index(pre[0])
        # 递归调用函数，遍历两个序列
        # 原树的左子树：前序遍历（从根节点一直到中心点），中序遍历（从开头一直到中心位置）
        root.left = self.reConstructBinaryTree(pre[1:val + 1], tin[:val])
        # 原树的右子树：前序遍历（从中心点后一直到叶子节点），中序遍历（同前序）
        root.right = self.reConstructBinaryTree(pre[val + 1:], tin[val + 1:])
        return root




