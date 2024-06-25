# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def check(node, has, res):
            if node == None:
                return "#"
            
            ls = check(node.left, has, res)
            rs = check(node.right, has, res)

            resStr = ','.join([str(node.val), ls, rs])
            if has[resStr] == 1:
                res.append(node)
            has[resStr] += 1

            return resStr

        has = collections.defaultdict(int)
        res = []
        k = check(root, has, res)
        return res