class Solution {
    class Pair{
        int x,y;
        Pair(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public int orangesRotting(int[][] grid) {
        int m=grid.length;
        int n=grid[0].length;

        int[][] vis=new int[m][n];
        Queue<Pair> q=new LinkedList<>();
        int[] dr={0,-1,1,0};
        int[] dc={-1,0,0,1};
        int ans=0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==2){
                    q.add(new Pair(i,j));
                    vis[i][j]=1;
                }
                if(grid[i][j]==1) 
                   ans=ans+1;         
            }
        }
        
        int c1=0;
        while(!q.isEmpty()){
            int s=q.size();
            c1=c1+1;
            for(int l=0;l<s;l++){
                Pair p=q.remove();
                for(int k=0;k<4;k++){
                    int r=p.x+dr[k];
                    int c=p.y+dc[k];
                    if(0<=r && r<m && 0<=c && c<n && vis[r][c]==0 && grid[r][c]==1)               { grid[r][c]=2;
                      vis[r][c]=1;
                      ans=ans-1;
                       q.add(new Pair(r,c));
                    }
                }
            }
        }
                  
        
        if(ans!=0) return -1;
        if(c1==0) return 0;
        return c1-1;
    }
}