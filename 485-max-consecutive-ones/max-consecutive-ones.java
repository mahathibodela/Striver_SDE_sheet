class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int c=-1,ans=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                ans=Math.max(ans,i-c-1);
                c=i;
            }
        }
        ans=Math.max(ans,nums.length-c-1);
        return ans;
    }
}