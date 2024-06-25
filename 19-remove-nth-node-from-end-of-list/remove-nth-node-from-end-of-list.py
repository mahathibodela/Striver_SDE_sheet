# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        s = f = head
        c = 0
        while c != n:
            f = f.next
            c += 1
        if f == None:
            return head.next

        while f.next != None:
            s = s.next
            f = f.next
        s.next = s.next.next if s.next else None
        return head
        