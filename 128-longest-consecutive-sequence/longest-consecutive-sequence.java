class Solution {
    public int longestConsecutive(int[] nums) {
        //WO SORT WALLA BHULNA MATH
        Set<Integer> set=new HashSet<>();
        for(int i=0;i<nums.length;i++){
            set.add(nums[i]);
        }
        int ans=0,c=0;
        for(int i:set){
            if(set.contains(i-1))
              continue;
            else{
                 int a=i;
                 while(set.contains(a)){
                     c=c+1;
                     a++;
                 }
                 ans=Math.max(ans,c);
                 c=0;
            }
        }
        return ans;
    }
}