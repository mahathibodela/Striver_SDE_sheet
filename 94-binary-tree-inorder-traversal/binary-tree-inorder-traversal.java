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
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> q=new Stack<>();
        List<Integer> ans=new ArrayList<>();
        TreeNode node=root,ptr=null;

        if(root==null)
          return ans;
        q.push(root);
        while(!q.isEmpty()){
            while(node.left!=null){
                node=node.left;
                q.push(node);
            }
            while(!q.isEmpty()){
                node=q.pop();
                ans.add(node.val);
                if(node.right!=null){
                   node=node.right;
                   q.push(node);
                   break;
              }  
            }
               
        }
        return ans;
    }
}