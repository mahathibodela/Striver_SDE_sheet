# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        ans = []
        ptr = root

        while True:
            while ptr != None:
                ans.append(ptr.val)
                if ptr.right != None:
                    stack.append(ptr.right)
                ptr = ptr.left
            
            if len(stack) != 0:
                ptr = stack[-1]
                stack.pop(-1)
            else:
                break
            
        return ans

        