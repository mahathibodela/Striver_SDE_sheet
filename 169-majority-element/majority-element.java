class Solution {
    public int majorityElement(int[] nums) {
       int c=0;
       int no=nums[0];
       int n=nums.length;

       for(int i=0;i<n;i++){
            if(no==nums[i])
              c=c+1;
            else{
                c=c-1;
                if(c==0){
                    no=nums[i];
                    c=1;
                }
            }
            
       }
       return no;
    }
}