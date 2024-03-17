class Solution {
    void check(int i,List<Integer> sa,List<List<Integer>> ans,int[] nums,int n){
        //List<Integer> a=new ArrayList<>(sa);
        ans.add(new ArrayList<>(sa));
        for(int j=i;j<n;j++){
            if(j==i || nums[j]!=nums[j-1]){
                sa.add(nums[j]);
                //ans.add(sa);
                check(j+1,sa,ans,nums,n);
                sa.remove(sa.size()-1);
            }
        }
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> sa=new ArrayList<>();
        int n=nums.length;
        // ans.add(sa);
        check(0,sa,ans,nums,n);
        return ans;
    }
}