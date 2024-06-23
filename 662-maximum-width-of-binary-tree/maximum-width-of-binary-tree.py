# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        q = [(root, 1)]
        ans = 0

        while q:
            s = len(q)
            f = -1
            e = -1

            for i in range(s):
                node, c = q.pop(0)
                if i == 0:
                    f = c
                if i == s-1:
                    e = c
                
                if node.left != None:
                    q.append((node.left, 2 * c + 1 - f))
                if node.right != None:
                    q.append((node.right, 2 * c + 2 - f))

            ans = max(ans, e - f + 1)
        
        return ans
                    



        