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
    public void flatten(TreeNode root) {
        Stack<TreeNode> s=new Stack<>();
        TreeNode ptr=root;
        if(root==null) return ;
        if(root.right!=null) s.push(root.right);

        while(ptr!=null || !s.isEmpty()){
            while(ptr.left!=null){
                ptr.right=ptr.left;
                ptr.left=null;
                ptr=ptr.right;
                if(ptr.right!=null)
                   s.push(ptr.right);
            }
            if(!s.isEmpty()){
                TreeNode temp=s.pop();
                ptr.right=temp;
                ptr.left=null;
                if(temp.right!=null)
                  s.push(temp.right);
                ptr=ptr.right;
            }
            else break;
        }

        return ;
    }
}