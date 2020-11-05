import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS后序遍历
class Solution:
    def dfs(self, root: TreeNode):
        if not root:
            return 0
        return max(self.dfs(root.left), self.dfs(root.right)) + 1


# 层序遍历/广度优先搜索, 通常使用队列实现
class Handler:
    def bfs(self, root: TreeNode):
        """
        特例处理： 当 root​ 为空，直接返回 深度 0。
        初始化： 队列 queue （加入根节点 root ），计数器 res = 0。
        循环遍历： 当 queue 为空时跳出。
        初始化一个空列表 tmp ，用于临时存储下一层节点；
        遍历队列： 遍历 queue 中的各节点 node ，并将其左子节点和右子节点加入 tmp；
        更新队列： 执行 queue = tmp ，将下一层节点赋值给 queue；
        统计层数： 执行 res += 1 ，代表层数加 1；
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1

        return res


x = math.sqrt(5)
print(x)
