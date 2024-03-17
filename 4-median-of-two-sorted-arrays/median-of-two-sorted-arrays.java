class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1=nums1.length,n2=nums2.length;
        
        if(n2==0){
            if(n1%2==1) return nums1[n1/2];
            else return (nums1[n1/2]+nums1[(n1/2)-1])/2.0;
        }
        if(n1>n2) return findMedianSortedArrays(nums2,nums1);
        int l=0,h=n1,cut1=0,cut2=0,l1=0,l2=0,h1=0,h2=0,mid;
        
        cut1=n1;
        while(l<=h){
           cut1=(l+h)>>1;
           cut2=((n1+n2+1)/2)-cut1;

           if(cut1==0) l1=-(int)1e9;
           else l1=nums1[cut1-1];
           if(cut2==0) l2=-(int)(1e9);
           else l2=nums2[cut2-1];

           if(cut1==n1) h1=(int)1e9;
           else h1=nums1[cut1];
           if(cut2==n2) h2=(int)1e9;
           else h2=nums2[cut2];

           
           if(l1>h2) h=cut1-1;
           else if(l2>h1) l=cut1+1;
           else{
               if((n1+n2)%2==0){
                   return ((Math.max(l1,l2)+Math.min(h1,h2))/2.0);
               }
               else return Math.max(l1,l2);
           }
        }

        return 0;
    }
}