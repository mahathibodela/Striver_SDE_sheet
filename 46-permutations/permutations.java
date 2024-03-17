class Solution {
    void swap(List<Integer> s,int i,int j){
        int temp=s.get(i);
        s.set(i,s.get(j));
        s.set(j,temp);
    }
    void check(int i,int[] nums,List<Integer> s,List<List<Integer>> ans){
        if(i==nums.length){
            ans.add(new ArrayList<>(s));
            return ;
        }

        for(int j=i;j<nums.length;j++){
            swap(s,i,j);
            check(i+1,nums,s,ans);
            swap(s,i,j);
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> s=new ArrayList<>();
        for(int i=0;i<nums.length;i++) s.add(nums[i]);
        check(0,nums,s,ans);
        return ans;
    }
}