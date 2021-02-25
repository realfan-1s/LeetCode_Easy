class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# N叉树的前序遍历, 递归解法
def PreorderRecursion(root: 'Node'):
    if not root:
        return []

    def dfs(root: 'Node', res: list):
        if not root:
            return

        res.append(root.val)

        if not root.children:
            return

        for child in root.children:
            dfs(child, res)

    res = []
    dfs(root, res)
    return res


# N叉树的前序遍历，迭代解法,利用栈，倒序添加孩子节点，保证左侧孩子始终处于栈顶
def PreorderIteration(root: 'Node'):
    if not root:
        return []
    res = []
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        res.append(node.val)
        stack.extend(node.children[::-1])

    return res


# N叉树的后序遍历
def postOrder(root: 'Node'):
    if not root:
        return []

    res = []
    stack = [
        root,
    ]
    while stack:
        node = stack.pop()
        if node is not None:
            res.append(node.val)
        for child in node.children:
            stack.append(child)

    return res[::-1]