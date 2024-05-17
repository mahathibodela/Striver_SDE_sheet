# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        q = []
        q.append((0, root))
        count = defaultdict(list)
        mini = 0
        maxi = 0

        while len(q) != 0:
            s = len(q)
            temp = defaultdict(list)

            for j in range(s):
                i, node = q.pop(0)
                temp[i].append(node.val)
                if node.left != None:
                    q.append((i-1, node.left))
                    mini = min(i-1, mini)
                if node.right != None:
                    q.append((i + 1, node.right))
                    maxi = max(maxi, i + 1)
    
            
            for key, value in temp.items():
                value.sort()
                for no in value:
                    count[key].append(no)
        
        ans = []
        for i in range(mini, maxi + 1):
            ans.append(count[i])
        
        return ans





            
