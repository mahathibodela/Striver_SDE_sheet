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
        heap = []
        heapq.heapify(heap)
        ans = ListNode(-1)
        temp = ans
        ptr = None

        for node in lists:
            if node != None:
                heapq.heappush(heap, (node.val, node))
        
        while len(heap) != 0:
            _, ptr = heapq.heappop(heap)
            ans.next = ptr
            ans = ans.next

            if ptr.next != None:
                heapq.heappush(heap, (ptr.next.val, ptr.next))
            
        
        return temp.next



        