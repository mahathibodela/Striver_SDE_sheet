class Solution {
    void dfs(int i,int j,char[][] grid,int[][] vis,int m,int n){
        vis[i][j]=1;
        int[] dr={0,-1,1,0};
        int[] dc={-1,0,0,1};

        for(int k=0;k<4;k++){
            int r=i+dr[k];
            int c=j+dc[k];
            if(0<=r && r<m && 0<=c && c<n && vis[r][c]==0 && grid[r][c]=='1'){
                dfs(r,c,grid,vis,m,n);
            }
        }
    }
    public int numIslands(char[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        int[][] vis=new int[m][n];
        int ans=0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(vis[i][j]==0 && grid[i][j]=='1'){
                    ans++;
                    dfs(i,j,grid,vis,m,n);
                }
            }
        }

        return ans;
    }
}