# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        ptr = root
        ans = []

        while ptr != None or stack:
            if ptr != None:
                stack.append(ptr)
                ptr = ptr.left
            else:
                temp = stack[-1].right
                if temp == None:
                    temp = stack[-1]
                    stack.pop(-1)
                    ans.append(temp.val)

                    while stack and stack[-1].right == temp:
                        temp = stack[-1]
                        stack.pop(-1)
                        ans.append(temp.val)

                else:
                    ptr = temp
        
        return ans

            



        