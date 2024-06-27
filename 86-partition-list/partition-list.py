# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-(10 ** 10))
        dummy.next = head

        lessPtr = head
        lessPre = dummy
        while lessPtr != None and lessPtr.val < x:
            lessPre = lessPtr
            lessPtr = lessPtr.next 
        if lessPtr == None:
            return head
        
        grePtr = lessPtr.next
        grePre = lessPtr
        while grePtr != None:
            if grePtr.val < x:
                lessPre.next = grePtr
                grePre.next = grePtr.next
                grePtr.next = lessPtr
                lessPre = lessPre.next

                grePtr = grePre.next
            else:
                grePre = grePtr
                grePtr = grePtr.next
        
        return dummy.next

        
        