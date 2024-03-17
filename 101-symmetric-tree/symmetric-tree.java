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
    boolean check(TreeNode ptr1,TreeNode ptr2){
        if(ptr1==null && ptr2==null) return true;
        if((ptr1!=null && ptr2==null) || (ptr1==null && ptr2!=null)) return false;

        if(ptr1.val==ptr2.val) 
           return check(ptr1.left,ptr2.right) && check(ptr1.right,ptr2.left);
        return false;
    }
    public boolean isSymmetric(TreeNode root) {
        if(root==null) return true;
        return check(root.left,root.right);
    }
}