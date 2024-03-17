class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n=nums.length;
        int[] ans=new int[n-k+1];
        int c=0;

        Deque<Integer> d=new ArrayDeque<>();
        for(int i=0;i<n;i++){
           
           if(!d.isEmpty()  && d.peek()==i-k){
               d.poll();
           }

           while(!d.isEmpty() && nums[d.peekLast()]<nums[i]){
               d.pollLast();
           }

           d.offer(i);

           if(i>=k-1){
               ans[c]=nums[d.peek()];
               c=c+1;
           }
        }
        return ans;
    }
}