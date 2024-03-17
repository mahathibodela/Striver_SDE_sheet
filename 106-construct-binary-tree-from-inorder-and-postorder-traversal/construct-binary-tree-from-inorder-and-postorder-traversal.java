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
TreeNode check(int[] postorder,int[] inorder,int[] pi,int l,int h,Map<Integer,Integer> mi,int n){
        if(pi[0]==-1 || (h<l)) return null ;

        int v=postorder[pi[0]];
        int ind=mi.get(v);
        TreeNode root=new TreeNode(inorder[ind],null,null);
        
        pi[0]=pi[0]-1;
        root.right=check(postorder,inorder,pi,ind+1,h,mi,n);
        root.left=check(postorder,inorder,pi,l,ind-1,mi,n);
        
        return root;
    }
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int n=inorder.length;
        int[] pi=new int[1];
        pi[0]=n-1;
        Map<Integer,Integer> mi=new HashMap<>();
        for(int i=0;i<inorder.length;i++) mi.put(inorder[i],i);

        return check(postorder,inorder,pi,0,n-1,mi,n);    
    }
}