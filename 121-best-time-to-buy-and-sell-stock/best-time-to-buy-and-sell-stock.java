class Solution {
    public int maxProfit(int[] prices) {
        int n=prices.length;
        int mini=prices[0];
        int maxpro=0;
        for(int i=1;i<n;i++){
            int cost=prices[i]-mini;
            maxpro=Math.max(cost,maxpro);
            mini=Math.min(mini,prices[i]);
        }
        return maxpro;
    }
}