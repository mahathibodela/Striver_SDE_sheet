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
        incStack = []
        decStack = []

        ptr = root
        while ptr != None:
            incStack.append(ptr)
            ptr = ptr.left
        
        ptr = root
        while ptr != None:
            decStack.append(ptr)
            ptr = ptr.right
        
        inc = incStack[-1]
        dec = decStack[-1]

        while inc.val < dec.val:

            if inc.val + dec.val < k:
                incStack.pop(-1)
                ptr = inc.right
                while ptr != None:
                    incStack.append(ptr)
                    ptr = ptr.left
                
                inc = incStack[-1]
            
            elif inc.val + dec.val > k:
                decStack.pop(-1)
                ptr = dec.left
                while ptr != None:
                    decStack.append(ptr)
                    ptr = ptr.right
                
                dec = decStack[-1]
            
            else:
                return True
        
        return False

            
        