class Solution {
    void check(List<Integer> s,List<List<Integer>> ans,int i,int[] candidates,int target){
        //SO LAST MAIN ANS MAINKARTHE TIME NEW BANAKE ADD KARNA
        //AND FIRST HAMEASHA PICK KARNA
        if(i==candidates.length) return ;
        if(target==0) {
            ans.add(new ArrayList<Integer>(s));
            return ;
        }
        //pick
        if(candidates[i]<=target){
            s.add(candidates[i]);
            check(s,ans,i,candidates,target-candidates[i]);
            s.remove(s.size()-1);      
        }
        //unpick
        check(s,ans,i+1,candidates,target);
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> s=new ArrayList<>();

        check(s,ans,0,candidates,target);
        return ans;
    }
}