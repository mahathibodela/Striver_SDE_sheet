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
 */
class Solution {
    int check(TreeNode root,int[] maxi){
        if(root==null) return 0;

        int lh=0,rh=0;
        if(root.left!=null) lh=check(root.left,maxi);
        if(root.right!=null) rh=check(root.right,maxi);
         
        if(Math.abs(lh-rh)>1) maxi[0]=0;
        //maxi[0]=Math.max(maxi[0],lh+rh);
        return 1+Math.max(lh,rh);
    }
    public boolean isBalanced(TreeNode root) {
        int[] maxi=new int[1];
        maxi[0]=1;
        int k=check(root,maxi);
        if(maxi[0]==0) return false;
        return true;
    }
}