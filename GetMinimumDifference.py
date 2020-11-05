class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 中序遍历,特点:二叉搜索树中序遍历得到的值序列是递增有序的
# 不管是先序中序还是后序，查找流程都是从上到下，先左后右。只是输出的时机不同。
class Solution:
    def InorderTraversal(self, root: TreeNode):
        # pre记录的是前驱节点
        self.pre = -1
        # ans记录的是差值的最小值
        self.ans = float("inf")
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode):
        """
        中序遍历递归
        """
        if root is None:
            return

        self.dfs(root.left)
        if self.pre == -1:
            self.pre = root.val
        else:
            self.ans = min(self.ans, root.val - self.pre)
            self.pre = root.val

        self.dfs(root.right)
