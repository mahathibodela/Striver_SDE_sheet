# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ans = ListNode(-1)
        ans.next = head

        ptr = head
        c = 0
        while ptr != None:
            c += 1
            ptr = ptr.next
        
        no = c / k

        prev = ans
        cur = head
        c = 0
        
        while cur != None and no != 0:
            start = prev 
            end = cur

            c = 0
            while c <  k and cur != None:
                fut = cur.next
                cur.next = prev
                prev = cur
                cur = fut
                c += 1

            no -= 1
                
            start.next = prev
            end.next = cur
            prev = end
        
        return ans.next