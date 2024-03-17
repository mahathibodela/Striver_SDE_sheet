/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    boolean check(TreeNode root,TreeNode[] ans,int a,int b){
        if(root==null) return false;

        boolean lh=false,rh=false;
        lh=check(root.left,ans,a,b);
        rh=check(root.right,ans,a,b);

        if(root.val==a || root.val==b){
            if(lh==true || rh==true){
                ans[0]=root;
                return false;
            }
            else return true;
        }
        else{
            if(lh==true && rh==true)
               ans[0]=root;  
        }

        return (lh||rh);
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode[] ans=new TreeNode[1];
        ans[0]=null;

        boolean s=check(root,ans,p.val,q.val);
        return ans[0];
    }
}