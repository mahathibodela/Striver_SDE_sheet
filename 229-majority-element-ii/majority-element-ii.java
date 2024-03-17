class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int c1=0,c2=0,e1=-(int)1e9,e2=-(int)1e9;
        for(int i=0;i<nums.length;i++){
            if(c1==0 && nums[i]!=e2){
                c1=1;
                e1=nums[i];
            }
            else if(c2==0 && nums[i]!=e1){
                c2=1;
                e2=nums[i];
            }
            else if(nums[i]==e1) c1++;
            else if(nums[i]==e2) c2++;
            else {
                c1--;c2--;
            }
        }
        c1=0;c2=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==e1)
              c1++;
            else if(nums[i]==e2)
              c2++;
        }
        List<Integer> ans=new ArrayList<>();
        if(c1>(nums.length)/3) ans.add(e1);
        if(c2>(nums.length)/3) ans.add(e2);

        return ans;
    }
}