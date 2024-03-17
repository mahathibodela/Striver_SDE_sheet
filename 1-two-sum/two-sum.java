class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer,Integer> map=new HashMap<>();
        // for(int i=0;i<nums.length;i++) map.put(nums[i],i);

        // Arrays.sort(nums);
        // int i=0,j=nums.length-1;
        int[] ans=new int[2];
        // while(i<j){
        //     if(nums[i]+nums[j]==target){
        //        ans[0]=map.get(nums[i]);
        //        ans[1]=map.get(nums[j]);
        //        return ans;
        //     }
        //     else if(nums[i]+nums[j]>target) j=j-1;
        //     else i=i+1;
        // }
        // return ans;
        //UPAR APPROCH DUPPLICATE KELIYE KAAM NEHI KAREGA BEY

        for(int i=0;i<nums.length;i++){
            if(map.containsKey(target-nums[i])){
                ans[0]=map.get(target-nums[i]);
                ans[1]=i;
                return ans;
            }
            else map.put(nums[i],i);
        }
        return ans;
    }
}