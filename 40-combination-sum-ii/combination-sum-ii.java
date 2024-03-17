class Solution {
    //THIS IS THE METHOD FOR GETTING NO DUPLICATES WITHOUT HAVING A SET....
    void check(List<Integer> s,List<List<Integer>> ans,int i,int[] candidates,int target){
        if(target==0){
            ans.add(new ArrayList<>(s));
            return ;
        }
        for(int j=i;j<candidates.length;j++){
            if(j==i || candidates[j]!=candidates[j-1]){
               if(candidates[j]<=target){
                target=target-candidates[j];
                s.add(candidates[j]);
                check(s,ans,j+1,candidates,target);
                target=target+candidates[j];
                s.remove(s.size()-1);            
               }
               else
                 return;
            }
           
        }
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> s=new ArrayList<>();

        check(s,ans,0,candidates,target);
        return ans;
    }
}