# 查找哈希表法
def Hash(head):
    headHash = {}
    while head:
        if head in headHash:
            return True
        else:
            headHash.add(head)
            head = head.next

    return False


# 快慢指针法
def TwoChars(head):
    if not head or not head.next:
        return False
    slowChar = head
    fastChar = head.next

    while slowChar != fastChar:
        if not fastChar or not fastChar.next:
            return False
        slowChar = slowChar.next
        fastChar = fastChar.next.next

    return True
