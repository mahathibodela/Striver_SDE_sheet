# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        q = []
        q.append(root)
        ans = ""

        while len(q) != 0:
            s = len(q)

            for i in range(s):
                node = q.pop(0)
                if node == None:
                    k = "#"
                else:
                    k = str(node.val)
                ans = ans + k + " "

                if node != None:
                    q.append(node.left)
                    q.append(node.right)
        
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        q = []
        data = data[:len(data) - 1]
        dataa = data.split(" ")
        print(dataa)
        if len(dataa) == 1 and dataa[0] == '#':
            return None
        
        root = TreeNode(dataa[0])
        c = 1
        q.append(root)

        while len(q) != 0 and c < len(dataa):
            node = q.pop(0)

            if dataa[c] != '#':
                node.left = TreeNode(dataa[c])
                q.append(node.left)
            c += 1
            
            if c < len(data) and dataa[c] != '#':
                node.right = TreeNode(dataa[c])
                q.append(node.right)
            c += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))