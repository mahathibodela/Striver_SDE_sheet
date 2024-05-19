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
        
        stack = []
        root = None

        for i in range(len(preorder)):
            node = TreeNode(preorder[i])
            if root == None: root = node
            
            temp = None
            while stack and stack[-1].val < node.val:
                temp = stack[-1]
                stack.pop(-1)
            
            if stack and temp == None:
                temp = stack[-1]
                temp.left = node
            elif temp != None:
                temp.right = node
            stack.append(node)
  

        return root