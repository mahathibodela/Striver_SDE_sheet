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
    int check(TreeNode root){
        if(root==null) return 0;

        int lh=0,rh=0;
        if(root.left!=null) lh=check(root.left);
        if(root.right!=null) rh=check(root.right);

        return 1+Math.max(lh,rh);
    }
    public int maxDepth(TreeNode root) {
        return check(root);  
    }
}