class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int lmax = height[0];
        int rmax = height[n - 1];
        int l = 0;
        int r = n - 1;
        int ans = 0;

        while (l < r){
            if (lmax <= rmax){
                l += 1;
                lmax = max(height[l], lmax);
                ans += lmax - height[l];
            }
            else{
                r -= 1;
                rmax = max(height[r], rmax);
                ans += rmax - height[r];
            }
        }

        return ans;
        
    }
};