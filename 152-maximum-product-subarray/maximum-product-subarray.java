class Solution {
    //krishna curmax and curmin are the continous max and min they dont stop okk
    //so we should not right like that okkk
    //u r good girllll!!!!!!!!
    public int maxProduct(int[] nums) {
        int max = Arrays.stream(nums).max().getAsInt();
        int curmax=1,curmin=1;

        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                curmax=1;
                curmin=1;
                continue;
            }
            else if(nums[i]>0){
                curmax=Math.max(curmax*nums[i],nums[i]);
                curmin=Math.min(curmin*nums[i],nums[i]);
            }
            else{
               int tempmin=curmin;
               int tempmax=curmax;
                curmax=Math.max(tempmin*nums[i],nums[i]);
                curmin=Math.min(tempmax*nums[i],nums[i]);
            }

            if(curmax>max)
              max=curmax;
           
        }
        
        return max;
    }
}