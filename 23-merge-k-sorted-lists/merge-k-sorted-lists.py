# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = []
        ans = ListNode(-1)
        ptr = ans

        for node in lists:
            if node == None: continue
            heapq.heappush(q, [node.val, node])
        
        while q:
            _, node = heapq.heappop(q)
            ptr.next = node
            ptr = ptr.next
            
            if node.next != None:
                node = node.next
                heapq.heappush(q, [node.val, node])
        
        return ans.next
        