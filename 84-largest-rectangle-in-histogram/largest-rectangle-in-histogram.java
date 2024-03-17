class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> ls=new Stack<>();
        Stack<Integer> rs=new Stack<>();
        int n=heights.length;
        int[] l=new int[n];
        int[] r=new int[n];
        int top=0;
        for(int i=0;i<n;i++){
           //pehle for ls
               
               while((!ls.isEmpty()) && heights[ls.peek()]>=heights[i]){
                   ls.pop();
               }
               if(ls.isEmpty()) l[i]=0;
               else l[i]=ls.peek()+1;
               ls.push(i);

           //ab rs walla part
             
                while((!rs.isEmpty()) && heights[rs.peek()]>=heights[n-1-i]){
                   rs.pop();
               }
               if(rs.isEmpty()) r[n-i-1]=n-1;
               else r[n-1-i]=rs.peek()-1;
               rs.push(n-i-1);
           
        }
        int maxi=0;
        for(int i=0;i<n;i++){
           maxi=Math.max(maxi,heights[i]*(r[i]-l[i]+1));
           System.out.println(l[i]+" here "+r[i]);
        }
        return maxi;
    }
}
