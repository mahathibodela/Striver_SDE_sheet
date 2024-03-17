/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
  int check(TreeNode root,int[] maxi){
        if(root==null) return 0;

        int left=Math.max(0,check(root.left,maxi));
        int right=Math.max(0,check(root.right,maxi));

        maxi[0]=Math.max(maxi[0],root.val+left+right);

        return root.val+Math.max(left,right);

    }
    public int maxPathSum(TreeNode root) {
        int[] maxi=new int[1];
        maxi[0]=-(int)(1e9);
        int a=check(root,maxi);
        //this function is giving tha max sum path either left or right bas not the ans
        return maxi[0];
    }
 */
class Solution {
    int check(TreeNode root,int[] ans){
        if(root==null) return 0;

        int ls=0,rs=0;
        ls=check(root.left,ans);
        rs=check(root.right,ans);
        
        int a=0;
        if(ls<0 && rs<0) a=0;
        else if(ls<=0 || rs<=0) a=Math.max(ls,rs);
        else a=ls+rs;

        ans[0]=Math.max(ans[0],a+root.val);

        return root.val+Math.max(Math.max(0,ls),Math.max(rs,0));
    }
    public int maxPathSum(TreeNode root) {
        int[] ans=new int[1];
        ans[0]=-(int)1e9;
        int k=check(root,ans);
        return ans[0];
    }
}