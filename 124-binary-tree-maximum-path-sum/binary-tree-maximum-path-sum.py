# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def check(node, ans):
            if node == None:
                return 0
            
            lsum = max(check(node.left, ans), 0)
            rsum = max(check(node.right, ans), 0)
            
            k = node.val + rsum + lsum
            ans[0] = max(ans[0], k)
            return node.val + max(lsum, rsum)
        
        ans = [-(10 ** 10)]
        check(root, ans)
        return ans[0]
        