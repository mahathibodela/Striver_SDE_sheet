class Solution {
    boolean check(int i,int s,int[] nums,int[][] dp,int n,int sum){
        if(sum==s) return true;
        if(i>=n || sum>s) return false;

        if(dp[i][sum]!=-1){
            if(dp[i][sum]==1) return true;
            return false;
        }
        boolean pick=false,unpick=false;
        pick=check(i+1,s,nums,dp,n,sum+nums[i]);
        unpick=check(i+1,s,nums,dp,n,sum);
        
        if(pick||unpick) dp[i][sum]=1;
        else dp[i][sum]=0;

        return pick||unpick;     
    }
    public boolean canPartition(int[] nums) {
        int n=nums.length;
        int sum=0;
        for(int i=0;i<n;i++){
          sum=sum+nums[i];
        }
        if(sum%2!=0) return false;

        int[][] dp=new int[n][sum/2];

        for(int i=0;i<n;i++){
            for(int j=0;j<sum/2;j++){
                dp[i][j]=-1;
            }
        }

        return check(0,sum/2,nums,dp,n,0);
    }
}