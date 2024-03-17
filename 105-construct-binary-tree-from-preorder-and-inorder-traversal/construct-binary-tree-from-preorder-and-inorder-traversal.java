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
TreeNode check(int[] preorder,int[] inorder,int[] pi,int l,int h,Map<Integer,Integer> mi,int n){
        if(pi[0]==n || (h<l)) return null ;

        int v=preorder[pi[0]];
        int ind=mi.get(v);
        TreeNode root=new TreeNode(inorder[ind],null,null);
        
        pi[0]=pi[0]+1;
        root.left=check(preorder,inorder,pi,l,ind-1,mi,n);
        root.right=check(preorder,inorder,pi,ind+1,h,mi,n);
        
        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int[] pi=new int[1];
        pi[0]=0;
        Map<Integer,Integer> mi=new HashMap<>();
        for(int i=0;i<inorder.length;i++) mi.put(inorder[i],i);
        int n=inorder.length;

        return check(preorder,inorder,pi,0,n-1,mi,n);       
    }
}