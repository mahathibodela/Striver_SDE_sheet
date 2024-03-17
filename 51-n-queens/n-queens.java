class Solution {
    List<String> construct(char[][] b){
        List<String> a=new ArrayList<>();
        int n=b.length;
        for(int i=0;i<n;i++){
            String c="";
            for(int j=0;j<n;j++){
                c=c+b[i][j];
            }
            a.add(c);
        }
        return a;
    }
    boolean isSafe(char[][] b,int r,int c){
        int n=b.length;
        for(int i=r-1;i>=0;i--){
            if(b[i][c]=='Q') return false;
        }
        int i=r-1,j=c-1;
        while(i>=0 && j>=0){
            if(b[i][j]=='Q') return false;
            i=i-1;
            j=j-1;
        }
        i=r-1;j=c+1;
        while(i>=0 && j<n){
            if(b[i][j]=='Q') return false;
            i=i-1;
            j=j+1;
        }
        return true;
    }
    void check(int r,char[][] b,List<List<String>> ans){
        if(r==b.length){
            ans.add(new ArrayList<>(construct(b)));
            return ;
        }
        for(int c=0;c<b.length;c++){
            if(isSafe(b,r,c)){
                b[r][c]='Q';
                check(r+1,b,ans);
                b[r][c]='.';
            }
        }
    }
    public List<List<String>> solveNQueens(int n) {
        char[][] b=new char[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                b[i][j]='.';
            }
        }
        List<List<String>> ans=new ArrayList<>();
        check(0,b,ans);
        return ans;
    }
}