# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def check(node):
            if node == None:
                return 0
            
            lh = check(node.left)
            rh = check(node.right)

            return 1 + max(lh, rh)
        return check(root)
        