class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        time = grid[0][0]
        q = [(grid[0][0], 0, 0)]
        heapq.heapify(q)
        ways = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        vis = set()
        vis.add((0, 0))
        n = len(grid)
        m = len(grid[0])

        while q:
            node, r, c = heapq.heappop(q)
            time = max(time, node)
            if r == n - 1 and c == m - 1:
                return time

            for dr, dc in ways:
                nr = r + dr
                nc = c + dc
                if 0 <= nr and nr < n and 0<= nc and nc < m and (nr, nc) not in vis:
                    vis.add((nr, nc))
                    heapq.heappush(q, (grid[nr][nc], nr, nc))
        
        return -1





        