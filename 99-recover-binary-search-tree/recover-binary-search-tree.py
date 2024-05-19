# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def check(node, ans, pre):
            if node == None:
                return None
            
            left = check(node.left, ans, pre)
            if pre[0] != None and pre[0].val > node.val:
                if len(ans) == 0:
                    ans.append(pre[0])
                    ans.append(node)
                else:
                    ans[1] = node
            
            pre[0] = node
            
            right = check(node.right, ans, pre)
            return node
        
        ans = []
        pre = [None]
        k = check(root, ans, pre)
        temp = ans[0].val
        ans[0].val = ans[1].val
        ans[1].val = temp
