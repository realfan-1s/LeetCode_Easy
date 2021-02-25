using System.Collections;
using System.Collections.Generic;
using System.Linq.Expressions;
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode (int x) { val = x; }
}
// 递归
public class Solution1 {
    public TreeNode ConvertBiNode (TreeNode root) {
        TreeNode ans = TreeNode (0);
        InOrder (root, ans);
        return ans.right;
    }
    public TreeNode InOder (TreeNode root, TreeNode ans) {
        if (root != null) {
            ans = InOder (root.left, ans);
            root.left = null;
            ans.right = root;
            ans = root;
            ans = InOder (root.right, ans);
        }
        return ans;
    }
}

// 非递归
public class Solution2 {
    public TreeNode ConvertBiNode (TreeNode root) {
        TreeNode dummy = new TreeNode (0);
        TreeNode head = dummy;
        TreeNode node = root;
        Stack<TreeNode> stack = new Stack<TreeNode> ();

        while (node != null || stack.Count > 0) {
            if (node != null) {
                stack.Push (node);
                node = node.left;
            } else {
                node = stack.Pop ();
                node.left = null;
                head.right = node;
                head = root;
                node = node.right;
            }
        }
        return dummy.right;
    }
}