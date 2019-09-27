# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(-1)
        prev = l3
        while (l1 and l2):
            if l1.val <= l2.val:
                prev.next=l1
                if (l1 != None): l1 = l1.next
            else:
                prev.next=l2
                if (l2 != None): l2 = l2.next
            prev=prev.next
        prev.next = l1 if l1 is not None else l2
        return l3.next