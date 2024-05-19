# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(node, left, right):
            if node == None:
                return True
            
            if node == root or left < node.val and node.val < right:
                return check(node.left, left, node.val) and check(node.right, node.val, right)

            return False

        return check(root, -(10 ** 10), (10**10))
        