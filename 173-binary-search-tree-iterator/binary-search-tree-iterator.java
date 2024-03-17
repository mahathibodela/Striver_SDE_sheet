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
class BSTIterator {
    Stack<TreeNode> s;
    public void put(TreeNode r){
        TreeNode ptr=r;
        while(ptr.left!=null){
           s.push(ptr.left);
           ptr=ptr.left;
        }
    }
    public BSTIterator(TreeNode root) {
        s=new Stack<>();
        s.push(root);
        put(root);
    }
    
    public int next() {
        if(s.size()==0) return -1;
        TreeNode temp=s.pop();
        if(temp.right!=null){
           s.push(temp.right);
           put(temp.right);
        }
        int c=temp.val;
        return c;
    }
    
    public boolean hasNext() {
        if(s.size()!=0) return true;
        return false;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */