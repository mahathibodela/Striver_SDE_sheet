# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        def check(ind, l, h):
            if ind[0] == len(preorder):
                return None
            
            root = TreeNode(preorder[ind[0]])
            ind[0] += 1

            if ind[0] < len(preorder) and l < preorder[ind[0]] < root.val:
                root.left = check(ind, l, root.val)
            
            if ind[0] < len(preorder) and root.val < preorder[ind[0]] < h:
                root.right = check(ind, root.val, h)
            
            return root


        ind = [0]
        return check(ind, -(10 ** 10), (10 ** 10))
        