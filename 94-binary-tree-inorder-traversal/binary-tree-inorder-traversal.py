# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        ans = []

        while cur != None:
            if cur.left == None:
                ans.append(cur.val)
                cur = cur.right
            
            else:
                ptr = cur.left
                while ptr.right != None and ptr.right != cur:
                    ptr = ptr.right
                
                if ptr.right == None:
                    ptr.right = cur
                    cur = cur.left
                if ptr.right == cur:
                    ans.append(cur.val)
                    ptr.right = None
                    cur = cur.right
        
        return ans


        