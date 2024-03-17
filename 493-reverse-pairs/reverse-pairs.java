class Solution {
    private static void merge(int[] arr, int low, int mid, int high) {
        ArrayList<Integer> temp = new ArrayList<>();
        int left = low;     
        int right = mid + 1; 

        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                temp.add(arr[left]);
                left++;
            } else {
                temp.add(arr[right]);
                right++;
            }
        }

        while (left <= mid) {
            temp.add(arr[left]);
            left++;
        }

        while (right <= high) {
            temp.add(arr[right]);
            right++;
        }

        for (int i = low; i <= high; i++) {
            arr[i] = temp.get(i - low);
        }
    }
    void count(int l,int m,int h,int[] arr,int[] ans){
        int r=m+1;
        int c=0;
        for(int i=l;i<=m;i++){
            while(r<=h && arr[i]>2*(long)arr[r]) r++;
            c=c+(r-m-1);
        }
        ans[0]=ans[0]+c;
    }
    public void mergeSort(int[] arr, int low, int high,String s,int[] ans) {
        if (low >= high) return;
        int mid = (low + high) / 2 ;
        mergeSort(arr, low, mid,s+'a',ans);  
        mergeSort(arr, mid + 1, high,s+'a',ans); 
        count(low,mid,high,arr,ans);
        merge(arr, low, mid, high);  
    }
    public int reversePairs(int[] nums) {
        int[] ans=new int[1];
        int n=nums.length;
        int[] arr=nums;
        mergeSort(nums,0,nums.length-1,"",ans);
        return ans[0];
    }
}