# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ptr, l = head, 0

        while ptr != None:
            ptr = ptr.next
            l += 1
        
        base_length = l/k
        extra = l % k
        ans = []
        cur = head

        for i in range(k):
            ans.append(cur)

            for j in range(base_length - 1 + (1 if extra else 0)):
                if cur == None:
                    break
                cur = cur.next
            
            extra -= (1 if extra else 0)
            if cur != None:
                temp = cur
                cur = cur.next
                temp.next = None
        
        return ans

        