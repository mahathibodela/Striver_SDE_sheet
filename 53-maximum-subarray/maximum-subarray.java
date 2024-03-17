class Solution {
    public int maxSubArray(int[] nums) {
        int cs=0,ms=-(int)(1e9);
        for(int i=0;i<nums.length;i++){
            cs=cs+nums[i];
            if(ms<cs)
               ms=cs;
            if(cs<0)
               cs=0;
        }
        return ms;
    }
}