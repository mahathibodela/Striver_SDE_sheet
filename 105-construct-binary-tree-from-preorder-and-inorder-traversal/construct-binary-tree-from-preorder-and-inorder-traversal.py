# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def check(preInd, ins, ine, inInd):
            if preInd[0] >= len(preorder):
                return None
            if ins > ine: return None

            k = preorder[preInd[0]]
            preInd[0] += 1
            ind = inInd[k]
            node = TreeNode(k)
            if ins == ine:
                return node
            
            node.left = check(preInd, ins, ind - 1, inInd)
            node.right = check(preInd, ind + 1, ine, inInd)
            
            return node

        inInd = {}
        for i in range(len(inorder)):
            inInd[inorder[i]] = i
        k = check([0], 0, len(inorder) - 1, inInd)
        return k
        