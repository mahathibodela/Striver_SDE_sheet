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
    class Pair{
        int x;
        TreeNode node;
        Pair(TreeNode node,int x){
            this.x=x;
            this.node=node;
        }
    }
    public int widthOfBinaryTree(TreeNode root) {
        Queue<Pair> q=new LinkedList<>();
        int ans=0;

        q.add(new Pair(root,1));
        while(!q.isEmpty()){
            int s=q.size();
            int f=0,l=0;
            for(int i=0;i<s;i++){
                Pair p=q.remove();
                if(i==0) f=p.x;
                if(i==s-1) l=p.x;

                if(p.node.left!=null) q.add(new Pair(p.node.left,2*p.x-f));
                if(p.node.right!=null) q.add(new Pair(p.node.right,2*p.x+1-f));
            }
            ans=Math.max(ans,l-f+1);
        }

        return ans;
    }
}