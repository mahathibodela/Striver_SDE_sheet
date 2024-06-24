class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        if source == target:
            return 0
        rev = collections.defaultdict(list)
        for i in range(len(routes)):
            for a in routes[i]:
                rev[a].append(i)
        

        q = []
        vis = set()
        nodeVis = set()
        src = rev[source]
        for buses in rev[source]:
            for i in routes[buses]:
                vis.add(buses)
                q.append(i)
                nodeVis.add(i)
        
        c = 1
        while q:
            s = len(q)

            for _ in range(s):
                node = q.pop(0)
                if node == target:
                    return c
                for buses in rev[node]:
                    if buses not in vis:
                        vis.add(buses)
                        for i in routes[buses]:
                            if i not in nodeVis:
                                nodeVis.add(i)
                                q.append(i)
            c += 1
        
        return -1




        