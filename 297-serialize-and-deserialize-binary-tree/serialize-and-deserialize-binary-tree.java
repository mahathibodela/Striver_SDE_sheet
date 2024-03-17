/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String s="";
        Queue<TreeNode> q=new LinkedList<>();
        if(root==null) return "";
        q.add(root);
        TreeNode ptr=root;

        while(!q.isEmpty()){
            TreeNode temp=q.remove();
            if(temp==null){
                s=s+"#"+" ";
                continue;
            }
            s=s+Integer.toString(temp.val)+" ";
            q.add(temp.left);
            q.add(temp.right);
        }
       
        System.out.println(s);
        return s;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if(data.length()==0) return null;
        String[] values=data.split(" ");
        TreeNode root=new TreeNode(Integer.parseInt(values[0]));
        int n=values.length;
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);

        for(int i=1;i<n;i++){
            TreeNode ptr=q.remove();
            if(!values[i].equals("#")){
                ptr.left=new TreeNode(Integer.parseInt(values[i]));
                q.add(ptr.left);
            }
            if(!values[++i].equals("#")){
                ptr.right=new TreeNode(Integer.parseInt(values[i]));
                q.add(ptr.right);
            }
        }
        
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));