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
    class Node{
        int v,l,h;
        Node(int v,int l,int h){
            this.v=v;
            this.l=l;
            this.h=h;
        }
    }
    Node check(TreeNode root,int[] ans){
        if(root==null){
            return new Node(0,(int)(1e9),-(int)(1e9));
        }
        if(root.left==null && root.right==null){
            ans[0]=Math.max(ans[0],root.val);
            return new Node(root.val,root.val,root.val);
        }

        Node lc=check(root.left,ans);
        Node rc=check(root.right,ans);

        if(lc.h<root.val && root.val<rc.l){
            int a=root.val+lc.v+rc.v;
            System.out.println(root.val+" "+ans[0]+" "+a);
            ans[0]=Math.max(ans[0],a);
            if(root.left==null)
              return new Node(a,root.val,rc.h);
            else if(root.right==null)
              return new Node(a,lc.l,root.val);
            return new Node(a,lc.l,rc.h);
        }
        return new Node(0,-(int)(1e9),(int)(1e9));
    }
    public int maxSumBST(TreeNode root) {
        int[] ans=new int[1];
        ans[0]=-(int)(1e9);
        Node n=check(root,ans);
        if(ans[0]<0) return 0;
        return ans[0];
    }
}