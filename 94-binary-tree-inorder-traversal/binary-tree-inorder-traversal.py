# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        ptr = root

        while True:
            while ptr != None:
                stack.append(ptr)
                ptr = ptr.left
            
            if len(stack) != 0:
                ptr = stack[-1]
                stack.pop(-1)
                ans.append(ptr.val)
                ptr = ptr.right
            else:
                break
            
        return ans



        