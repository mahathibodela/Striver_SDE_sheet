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
    void inorder(TreeNode root, int k,int[] ans,int[] c){
        if(root.left!=null)  inorder(root.left,k,ans,c);

        c[0]=c[0]+1;
        if(k==c[0]) ans[0]=root.val;
        if(root.right!=null) inorder(root.right,k,ans,c);
    }
    public int kthSmallest(TreeNode root, int k) {
        int[] ans=new int[1];
        int[] c=new int[1];
        inorder(root,k,ans,c);
        return ans[0];
    }
}