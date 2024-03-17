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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans=new ArrayList<>();
        Queue<TreeNode> q=new LinkedList<>();
        if(root==null) return ans;

        int c=0;
        q.add(root);
        while(!q.isEmpty()){
            int k=q.size();
            List<Integer> l=new ArrayList<>();
            for(int i=0;i<k;i++){
               TreeNode ptr=q.remove();
                if(c%2==0)
                  l.add(ptr.val);
                else
                  l.add(0,ptr.val);

               if(ptr.left!=null) q.add(ptr.left);
               if(ptr.right!=null) q.add(ptr.right);
            }
            c=c+1;
            ans.add(l);
        }

        return ans;
    }
}