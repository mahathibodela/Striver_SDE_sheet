class Solution {
    public String longestPalindrome(String s) {
        int n=s.length();
        int[][] dp=new int[n][n];
        int maxi=1;
        int st=0,en=0;
        for(int i=n-1;i>=0;i--){
            for(int j=i;j<n;j++){
                int c=0;
                if(i==j) dp[i][j]=1;
                else{
                    if(s.charAt(i)==s.charAt(j)){
                        if(j==i+1) {
                            dp[i][j]=1;
                            c=1;
                        }
                        else if(dp[i+1][j-1]==1){
                           dp[i][j]=1;
                           c=1;
                        }
                    }       
                }
                if(j-i+1>=maxi && c==1){
                    maxi=j-i+1;
                    st=i;
                    en=j;
                }
            }
        }
        return s.substring(st,en+1);
    }
}