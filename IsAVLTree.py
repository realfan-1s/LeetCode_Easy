class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 后序遍历 + 剪枝 （从底至顶）
def isBalanced(root: TreeNode):
    def dfs(root: TreeNode):
        if not root:
            return 0
        left = dfs(root.left)
        # 叶节点的高度设置为-1
        if left == -1:
            return -1
        right = dfs(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1

    return dfs(root) != -1


# 前序遍历+ 判断深度 （从顶至底）
class Solution:
    def IsBalanced(self, root: TreeNode):
        if not root:
            return True
        return abs(self.DFS(root.left) -
                   self.DFS(root.right)) <= 1 and self.IsBalanced(
                       root.left) and self.IsBalanced(root.right)

    def DFS(self, root: TreeNode):
        if not root:
            return 0
        return max(self.DFS(root.left), self.DFS(root.right)) + 1