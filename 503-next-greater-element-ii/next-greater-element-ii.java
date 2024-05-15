class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n=nums.length;
        int[] ans=new int[n];
        for(int i=0;i<n;i++) ans[i]=-1;
        Stack<Integer> s=new Stack<>();
        s.push(0);
        int l=2*n-1;

        for(int i=1;i<=l;i++){
            System.out.println(i+" and "+i%n);

            int c=s.peek();
            
            if(nums[c]<nums[i%n]){
                while(s.size()!=0 && nums[s.peek()]<nums[i%n]){
                    int k=s.pop();
                    ans[k]=nums[i%n];
                }
                s.push(i%n);
            }
            else
            s.push(i%n);
        }
        return ans;
    }
}