class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    若两链表相交，两个指针分别走了(a + b + c)步后在交汇处相遇
    时间复杂度O(n)
    """
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        pivotForA, pivotForB = headA, headB
        while pivotForA != pivotForB:
            if pivotForA:
                pivotForA = pivotForA.next
            else:
                pivotForA = headB

            if pivotForB:
                pivotForB = pivotForB.next
            else:
                pivotForB = headA

        return pivotForB
