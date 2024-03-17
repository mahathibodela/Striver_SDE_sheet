class Solution {
    public void nextPermutation(int[] nums) {
        List<Integer> nu=new ArrayList<>();

        int n=nums.length;
        int b=-1;
        for(int i=n-1;i>0;i--){
            if(nums[i]>nums[i-1]){
                System.out.println(i-1);
                b=i-1;
                break;
            }
        }

        if(b==-1){
            Arrays.sort(nums);
            return ;
        }

        for(int i=n-1;i>b;i--){
            if(nums[i]>nums[b]){
                System.out.println(i);
                int temp=nums[b];
                nums[b]=nums[i];
                nums[i]=temp;
                break;
            }
        }

        for(int i=n-1;i>b;i--){
            nu.add(nums[i]);
        }
        
        int c=b+1;
        for(int i:nu){
           nums[c++]=i;
        }

    }
}