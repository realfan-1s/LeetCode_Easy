# 双链表法，时间复杂度为O(N),空间复杂度为O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def TwoPointers(head: ListNode, x: int):
    before = beforeHead = ListNode(0)
    after = afterHead = ListNode(0)
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    # 双链表合并
    after.next = None
    before.next = afterHead.next

    return beforeHead.next