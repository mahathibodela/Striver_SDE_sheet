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
        if root == None: return []
        q = []
        q.append((root, 1))
        ans = 0

        while len(q) != 0:
            s = len(q)
            f = l = 0
            for i in range(s):
                node, no = q.pop(0)
                if i == 0:
                    f = no
                if i == s - 1:
                    l = no
                
                if node.left != None: q.append((node.left, 2 * no - f))
                if node.right != None: q.append((node.right, 2 * no + 1 - f))
            
            print(l, f)
            ans = max(ans, l - f + 1)
        
        return ans

        
        