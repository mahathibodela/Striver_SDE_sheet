# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def check(node, ans):
            if node == None:
                return (0, 0)
            
            (ll, lr) = check(node.left, ans)
            (rl, rr) = check(node.right, ans)

            ans[0] = max(ans[0], max(lr, rl) + 1)
            return (lr + 1, rl + 1)
        

        ans = [0]
        a, b = check(root, ans)
        return ans[0] - 1
