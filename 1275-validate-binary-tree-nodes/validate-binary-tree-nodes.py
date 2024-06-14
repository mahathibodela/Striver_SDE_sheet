class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        # all conected 
        # and every node should have one way to be visited

        indeg = [0 for i in range(n)]
        outdeg = [0 for i in range(n)]

        for i in range(n):
            if leftChild[i] != -1:
                indeg[leftChild[i]] += 1
                outdeg[i] += 1
            if rightChild[i] != -1:
                indeg[rightChild[i]] += 1
                outdeg[i] += 1
        
        root = []
        for i in range(n):
            if indeg[i] == 0 and outdeg != 0:
                root.append(i)

        if len(root) != 1: return False


        def check(ind, vis): 
            vis.add(ind)
            if leftChild[ind] != -1:
                if leftChild[ind] in vis: return False

                if check(leftChild[ind], vis) == False:
                    return False
            if rightChild[ind] != -1:
                if rightChild[ind] in vis: return False

                if check(rightChild[ind], vis) == False:
                    return False
            
            return True
        
        vis = set()
        if check(root[0], vis) == False:
            return False

        if len(vis) == n:
            return True
        return False
        