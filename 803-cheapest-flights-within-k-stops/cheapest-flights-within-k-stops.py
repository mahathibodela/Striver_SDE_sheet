class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        adj = collections.defaultdict(list)
        for a, b, c in flights:
            adj[a].append([b, c])

        q = [(0, src)] # cost, node, steps
        dis = [(10 ** 10) for i  in range(n)]
        dis[src] = 0
        c = 0

        while q:
            s = len(q)

            for _ in range(s):
                cost, node = q.pop(0)

                for adjNode, adjCost in adj[node]:
                    if adjCost + cost < dis[adjNode]:
                        dis[adjNode] = adjCost + cost 
                        q.append((dis[adjNode], adjNode))
            
            if c == k :
                break
            c += 1
            
            print(dis[dst])
        
        if dis[dst] != 10 ** 10:
            return dis[dst]
        return -1
                

            