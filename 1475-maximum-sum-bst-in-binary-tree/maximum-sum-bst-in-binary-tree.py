# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def check(node, ans):
            if node == None:
                return ((10 ** 10), -(10 ** 10), 0)
            

            ll, lh, ls = check(node.left, ans)
            rl, rh, rs = check(node.right, ans)

            
            if lh < node.val and node.val < rl:
                ans[0] = max(ans[0], ls + rs + node.val)
                return (min(ll, node.val), max(rh, node.val), node.val + ls + rs)
            
            return (-(10 ** 10), (10 ** 10), -1)
        
        ans = [0]
        a, b, c = check(root, ans)

        return ans[0]