# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        def reverse(ptr, left, lpre):
            pre = None
            cur = ptr

            while left <= right:
                fut = cur.next
                cur.next = pre
                pre = cur
                cur = fut
                left += 1

            ptr.next = cur
            lpre.next = pre

        dummy = ListNode(-1)
        dummy.next = head

        ptr = head
        pre = dummy

        count = 1
        while count < left:
            pre = ptr
            ptr = ptr.next
            count += 1
        
        reverse(ptr, count, pre)
        return dummy.next