# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ptr1 = l1
        ptr2 = l2
        ans = ListNode(-1)
        ptr = ans

        c = 0
        while ptr1 != None or ptr2 != None or c != 0:
            a = ptr1.val if ptr1  else 0
            b = ptr2.val if ptr2  else 0

            d = a + b + c
            if d > 9:
                c = 1
                d = d % 10
            else:
                c = 0
            temp = ListNode(d)
            ptr.next = temp
            ptr = temp

            ptr1 = ptr1.next if ptr1  else None
            ptr2 = ptr2.next if ptr2  else None
        
        return ans.next
        



        