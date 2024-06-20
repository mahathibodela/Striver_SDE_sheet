class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = deque()
        n,m=len(mat),len(mat[0])
        vis=set()

        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j))
                    vis.add((i,j))

        l=0
        while(len(q)!=0):
            s=len(q)
            for j in range(s):
                r,c=q.popleft()
                direct=[[0,1],[-1,0],[0,-1],[1,0]]
                
                for dr,dc in direct:
                    nr=r+dr
                    nc=c+dc
                    if(0<=nr and nr<n and 0<=nc and nc<m and (nr,nc) not in vis):
                        vis.add((nr,nc))
                        mat[nr][nc]=l+1
                        q.append((nr,nc))
            l+=1
        return mat

