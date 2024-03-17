class Solution {
    int check(String word1, String word2,int i,int j,int[][] dp){
        if(i<0) return j+1;
        if(j<0) return i+1;

        if(dp[i][j]!=-1) return dp[i][j];
        
        int ans=0;
        if(word1.charAt(i)==word2.charAt(j))
           ans=check(word1,word2,i-1,j-1,dp);
        else{
            int insert=1+check(word1,word2,i,j-1,dp);
            int delete=1+check(word1,word2,i-1,j,dp);
            int replace=1+check(word1,word2,i-1,j-1,dp);
            ans=Math.min(insert,Math.min(delete,replace));
        }

        dp[i][j]=ans;
        return ans;
    }
    public int minDistance(String word1, String word2) {
        int n1=word1.length(),n2=word2.length();
        int[][] dp=new int[n1][n2];
        for(int i=0;i<n1;i++){
            for(int j=0;j<n2;j++){
                dp[i][j]=-1;
            }
        }
        return check(word1,word2,n1-1,n2-1,dp);
    }
}