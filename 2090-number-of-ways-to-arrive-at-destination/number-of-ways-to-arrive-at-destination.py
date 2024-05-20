import heapq
from collections import defaultdict

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        # Create adjacency list
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Priority queue (min-heap)
        heap = []
        dist = [float('inf')] * n
        count = [0] * n
        
        # Assuming source node is 0
        src = 0
        count[src] = 1
        dist[src] = 0
        heapq.heappush(heap, (0, src))

        # Dijkstra's algorithm with path counting
        while heap:
            current_dist, node = heapq.heappop(heap)

            for adjNode, edgWei in adj[node]:
                if current_dist + edgWei < dist[adjNode]:
                    dist[adjNode] = current_dist + edgWei
                    count[adjNode] = count[node]
                    heapq.heappush(heap, (dist[adjNode], adjNode))
                elif current_dist + edgWei == dist[adjNode]:
                    count[adjNode] = (count[adjNode] + count[node]) % (10 ** 9 + 7)

        return count[n - 1]
