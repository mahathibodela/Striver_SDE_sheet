class minsort implements Comparator<Integer>{
    public int compare(Integer a,Integer b){
        if(b<a) return 1;
        else if(b==a) return 0;
        return -1;
    }
}
class KthLargest {
    int k=0;
    Queue<Integer> q;
    public KthLargest(int k, int[] nums) {
        this.k=k;
        q=new PriorityQueue<>(new minsort());
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(q.size()<k){
                q.add(nums[i]);
            }
            else{
                int t=q.peek();
                if(nums[i]>t){
                    int d=q.remove();
                    q.add(nums[i]);
                }
            }
        }
    }
    
    public int add(int val) {
        if(q.size()<k){
            q.add(val);
            return q.peek();
        }
        int temp=q.peek();
        if(val>temp){
            int d=q.remove();
            q.add(val);
        }
        return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */