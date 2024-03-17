class Solution {
    int check(int i,int j,int[] a,int[][] dp){
        if(i>j) return 0;
        
        if(dp[i][j]!=-1) return dp[i][j];

        int mini=(int)(1e9);
        for(int k=i;k<=j;k++){
            int value=a[j+1]-a[i-1]+check(i,k-1,a,dp)+check(k+1,j,a,dp);
            mini=Math.min(mini,value);
        }
        return dp[i][j]=mini;
    }
    public int minCost(int n, int[] cuts) {
        int s=cuts.length;
        int[] a=new int[s+2];
        a[0]=0;
        Arrays.sort(cuts);
        for(int i=0;i<s;i++){
            a[i+1]=cuts[i];
        }
        a[s+1]=n;

        int[][] dp=new int[s+1][s+1];
        for(int i=0;i<s+1;i++){
            for(int j=0;j<s+1;j++){
                dp[i][j]=-1;
            }
        }
        return check(1,s,a,dp);
        
    }
}