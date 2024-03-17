class Solution {
    //DUPLICATE DECTECTION
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        Set<List<Integer>> set=new HashSet<>();
        List<List<Integer>> ans=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(i!=0 && nums[i]==nums[i-1]) continue;
            for(int j=i+1;j<nums.length;j++){
                if(j!=i+1 && nums[j]==nums[j-1]) continue;
                int l=j+1,h=nums.length-1;
                long sum=(long)target-nums[i]-nums[j];
                System.out.println(sum+" "+target);
                while(l<h){
                    long ss=(long)nums[l]+nums[h];
                    if(ss==sum){
                        List<Integer> a=new ArrayList<>();
                        a.add(nums[i]);
                        a.add(nums[j]);
                        a.add(nums[l]);
                        a.add(nums[h]);
                        ans.add(a);
                        l=l+1;
                        h=h-1;
                        while(l<h && nums[l]==nums[l-1]) l++;
                        while(l<h && nums[h]==nums[h+1]) h--;
                    }
                    else if(ss>sum) h=h-1;
                    else l=l+1;
                }
            }
        }
        return ans;
    }
}