# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def check(node):
            if node == None:
                return None
            
            l = check(node.left)
            r = check(node.right)


            if node.val > high:
                return l
            if node.val < low:
                return r
            node.left = l
            node.right = r
            return node
        
        return check(root)
