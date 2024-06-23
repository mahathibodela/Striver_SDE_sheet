# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        left = []
        right = []
        ptr = root
        while ptr != None:
            left.append(ptr)
            ptr = ptr.left
        ptr = root
        while ptr != None:
            right.append(ptr)
            ptr = ptr.right
        
        while left and right and left[-1].val < right[-1].val:
            a = left[-1].val
            b = right[-1].val

            if a + b == k:
                return True
            if a + b > k:
                ptr = right.pop(-1)
                if ptr.left != None:
                    ptr = ptr.left
                    while ptr != None:
                        right.append(ptr)
                        ptr = ptr.right
            else:
                ptr = left.pop(-1)
                if ptr.right != None:
                    ptr = ptr.right
                    while ptr != None:
                        left.append(ptr)
                        ptr = ptr.left
        
        return False


        