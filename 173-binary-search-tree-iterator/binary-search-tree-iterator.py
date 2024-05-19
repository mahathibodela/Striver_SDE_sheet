# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        ptr = root
        while ptr != None:
            self.stack.append(ptr)
            ptr = ptr.left
        

    def next(self):
        """
        :rtype: int
        """
        ptr = self.stack[-1]
        self.stack.pop(-1)
        c = ptr.val
        if ptr.right != None:
            ptr = ptr.right
            while ptr != None:
                self.stack.append(ptr)
                ptr = ptr.left
        
        return c
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack)!= 0:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()