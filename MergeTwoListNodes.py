class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.count = 0


# 暴力解法,引入哑节点,时间复杂度O(m+n),空间复杂度O(1)
class Solution:
    def MergeTwoLists(self,l1,l2):
        prevHead = ListNode(-1)
        prev = prevHead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        prev.next = l1 if l1 is not None else l2
        return prevHead.next


# 递归解法
class Recursion:
    def MergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.MergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.MergeTwoLists(l1, l2.next)
            return l2