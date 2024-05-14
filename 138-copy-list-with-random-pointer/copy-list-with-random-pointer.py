"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mapping = {}
        ptr = head
        mapping[None] = None

        while ptr != None:
            temp = Node(ptr.val)
            mapping[ptr] = temp
            ptr = ptr.next
        
        ptr = head
        copyHead = None
        while ptr != None:
            copy = mapping[ptr]
            if copyHead == None:
                copyHead = copy
            copy.next = mapping[ptr.next]
            copy.random = mapping[ptr.random]
            ptr = ptr.next
        
        return copyHead

        