class Solution {
    int check(int node,int[][] dp,int n,int[] coins,int tar){
        if(tar==0) return 0;
        if(node==0){
            if(tar%coins[0]==0) return tar/coins[0];
            return (int)(1e9);
        }

        if(dp[node][tar]!=-1) return dp[node][tar];
        int notpick=check(node-1,dp,n,coins,tar);
        int pick=(int)(1e9);

        if(coins[node]<=tar) 
            pick=1+check(node,dp,n,coins,tar-coins[node]);
        dp[node][tar]=Math.min(pick,notpick);
        
        return dp[node][tar];
    }
    public int coinChange(int[] coins, int amount) {
        int n=coins.length;
        // if(n==1){
        //     if(amount%coins[0]==0) return amount/coins[0];
        //     return -1 ;
        // }
        if(amount==0) return 0;
        int[][] dp=new int[n][amount+1];
        for(int i=0;i<n;i++){
            for(int j=0;j<amount+1;j++){
                dp[i][j]=-1;
            }
        }
        for(int i=1;i<amount+1;i++) {
            if(i>=coins[0] && i%coins[0]==0) dp[0][i]=i/coins[0];
            else dp[0][i]=(int)(1e9);
        }
        for(int i=1;i<n;i++){
            for(int j=0;j<amount+1;j++){
                if(j==0) dp[i][j]=0;
                else{
                    int notpick=dp[i-1][j];
                    int pick=(int)(1e9);
                    if(coins[i]<=j) pick=1+dp[i][j-coins[i]];
                    int ans=Math.min(pick,notpick);
                    dp[i][j]=ans;
                }
            }
        }
        if(dp[n-1][amount]==(int)(1e9)) return -1; else return dp[n-1][amount];
        // if(check(n-1,dp,n,coins,amount)==(int)(1e9)) return -1;
        // return check(n-1,dp,n,coins,amount);
    }
}