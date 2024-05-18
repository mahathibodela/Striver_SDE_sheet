# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p = p.val
        q = q.val
        def check(node, ans):
            if node == None:
                return 10 ** 10
            
            lh = check(node.left, ans)
            if lh == -(10 ** 10): return -(10 ** 10)
            rh = check(node.right, ans)
            if rh == -(10 ** 10): return -(10 ** 10)

            if (node.val == p or node.val == q):
                if (lh == q or lh == p or rh == q or rh == p):
                    ans.append(node)
                else:
                    return node.val
            elif (lh == p or lh == q):
                if rh == q or rh == p:
                    ans.append(node)
                else:
                    return lh
            elif rh == q or rh == p:
                return rh
            
            if len(ans) != 0:
                return -(10 ** 10)
            return 10 ** 10

        ans = []
        k = check(root, ans)
        return ans[0]
        