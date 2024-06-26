class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur = 0;
        int maxi = nums[0];
        int n = nums.size();

        for(int i = 0; i < n; i ++){
            cur += nums[i];
            maxi = max(maxi, cur);
            cur = max(cur, 0);
        }

        return maxi;

        
    }
};