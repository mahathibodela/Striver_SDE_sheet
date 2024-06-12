class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        def findParent(node):
            if parent[node] != node:
                parent[node] = findParent(parent[node])
            
            return parent[node]

        maxRow = maxCol = 0
        for u, v in stones:
            maxRow = max(maxRow, u)
            maxCol = max(maxCol, v)

        maxRow += 1
        maxCol += 1
        n = maxRow + maxCol
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        hasStones = set()

        for u, v in stones:
            up = findParent(u)
            vp = findParent(maxRow + v)
            hasStones.add(up)
            hasStones.add(vp)

            if up == vp:
                continue
            if size[up] > size[vp]:
                parent[vp] = up
                size[up] += size[vp]
            else:
                parent[up] = vp
                size[vp] += size[up]
        

        tot = 0
        for i in hasStones:
            if i == parent[i]:
                tot += 1
        
        return len(stones) - tot
            

     

        