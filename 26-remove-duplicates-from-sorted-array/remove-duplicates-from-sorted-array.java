class Solution {
    public int removeDuplicates(int[] nums) {
        int k=0,c=0,n=nums.length;
       
        for(int i=1;i<n;i++){
            if(nums[i]!=nums[i-1]){
                if(k==0){
                    nums[k]=nums[i-1];
                    k=k+1;
                }
                nums[k]=nums[i];
                k=k+1;
            }
        }
        if(k==0) return 1;
        return k;
    }
}