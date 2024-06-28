# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def check(node, pre):
            if node == None:
                return 
            
            pre[0].left = None
            pre[0].right = node
            pre[0] = node

            curRight = node.right
            check(node.left, pre)
            check(curRight, pre)
        

        dummy = TreeNode(-1)
        pre = [dummy]
        check(root, pre)

        return dummy.right