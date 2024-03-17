class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i=0,j=0,k=0;
        int temp=0;
        while(i<m && j<n){
            if(nums1[i]<=nums2[j]){  
               i=i+1;
            }
            else{
               temp=nums2[j];
               nums2[j]=nums1[i];
               nums1[i]=temp;
               i=i+1;
               Arrays.sort(nums2);
            }
        }
        for(;j<n;j++){
            nums1[i]=nums2[j];
            i=i+1;
        }
       
    }
}