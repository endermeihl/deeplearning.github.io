def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    first = 0
    second = 0
    carry = 0
    re = ListNode(0)
    r = re
    while (l1 or l2):
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = carry + x + y
        carry = s // 10
        r.next = ListNode(s % 10)
        r = r.next
        if (l1 != None): l1 = l1.next
        if (l2 != None): l2 = l2.next
    if (carry > 0):
        r.next = ListNode(1)
    return re.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]
addTwoNumbers(1, l1, l2)
