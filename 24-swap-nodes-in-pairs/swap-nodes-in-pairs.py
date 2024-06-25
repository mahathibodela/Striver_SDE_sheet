# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(-1)
        ans.next = head
        
        prev = ans
        cur = head
        while cur != None:
            start = prev 
            end = cur

            c = 0
            while c < 2 and cur != None:
                fut = cur.next
                cur.next = prev
                prev = cur
                cur = fut
                c += 1
            start.next = prev
            end.next = cur
            prev = end
        
        return ans.next

        