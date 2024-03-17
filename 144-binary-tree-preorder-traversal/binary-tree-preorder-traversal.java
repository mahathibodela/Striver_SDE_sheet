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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans=new ArrayList<>();
        Stack<TreeNode> q=new Stack<>();
        TreeNode ptr=root;
        if(root==null)
           return ans;
        if(root.right!=null)
           q.push(root);
        ans.add(root.val);
        while(ptr!=null ||!q.isEmpty()){
            while(ptr.left!=null){
                ptr=ptr.left;
                ans.add(ptr.val);
                if(ptr.right!=null){
                    q.push(ptr);
                }
            }
            if(!q.isEmpty()){
               ptr=q.pop();
               ptr=ptr.right;
               if(ptr.right!=null){
                   q.push(ptr);
               }
               ans.add(ptr.val); 
            }
            else break;
        }
        return ans;
    }
}