class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        q = []
        adj = defaultdict(list)
        indeg = [0 for i in range(numCourses)]
        for u, v in prerequisites:
            indeg[u] += 1
            adj[v].append(u)
        
        vis = set()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
                vis.add(i)
        
        ans = []
        while q:
            node = q.pop(0)
            ans.append(node)

            for adjNode in adj[node]:
                if adjNode not in vis:
                    indeg[adjNode] -= 1
                    if indeg[adjNode] == 0:
                        q.append(adjNode)
        
        if len(ans) == numCourses:
            return ans
        return []
                
        