# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def check(node, ans, an):
            if node == None:
                return None
            
            check(node.left, ans, an)
            ans[0] += 1
            if ans[0] == k:
                an.append(node.val)
            check(node.right, ans, an)
            
            return node


        ans = [0]
        an = []
        check(root, ans, an)
        return an[0]
        