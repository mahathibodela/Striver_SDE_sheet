class Solution {
    class Pair{
        int x,y;
        Pair(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int ic=image[sr][sc];
        int m=image.length;
        int n=image[0].length;
        int[][] vis=new int[m][n];

        vis[sr][sc]=1;
        Queue<Pair> s=new LinkedList<>();
        s.add(new Pair(sr,sc));
        int[] dr={0,-1,+1,0};
        int[] dc={-1,0,0,1};

        while(!s.isEmpty()){
            Pair p=s.remove();
            image[p.x][p.y]=color;
            for(int i=0;i<4;i++){
                int r=p.x+dr[i];
                int c=p.y+dc[i];
                if(0<=r && r<m && 0<=c && c<n && vis[r][c]==0 && image[r][c]==ic){
                    vis[r][c]=1;
                    s.add(new Pair(r,c));
                }
            }
        }

        return image;
    }
}