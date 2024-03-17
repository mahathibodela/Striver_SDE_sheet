class Solution {
    int check(String text1, String text2,int i,int j,int[][] dp){
        if(i==0 || j==0) return 0;

        if(dp[i][j]!=-1) return dp[i][j];
        
        int ans=0;
        if(text1.charAt(i - 1)==text2.charAt(j - 1)) 
            ans=1+check(text1,text2,i-1,j-1,dp);
        else
            ans=Math.max(check(text1,text2,i-1,j,dp),check(text1,text2,i,j-1,dp));
        
        dp[i][j]=ans;
        return ans;
         
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int n1=text1.length(),n2=text2.length();
        int[][] dp=new int[n1 + 1][n2+ 1];
        for(int i=0;i<=n1;i++){
            for(int j=0;j<=n2;j++){
                dp[i][j]=-1;
            }
        }
        
        for(int i = 0; i <= n1; i++){
            for(int j = 0; j <= n2; j++){
                if(i == 0 || j == 0)
                    dp[i][j] = 0;
                else{
                    if(text1.charAt(i - 1) == text2.charAt(j - 1)){
                        dp[i][j] = 1 + dp[i - 1][j - 1];
                    }
                    else{
                        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                    }
                }
            }
        }
        return dp[n1][n2];
        // return check(text1,text2,n1,n2,dp);
    }
}