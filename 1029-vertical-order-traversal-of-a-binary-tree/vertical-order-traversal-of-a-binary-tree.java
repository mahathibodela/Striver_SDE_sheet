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
    class Tuple{
        int x,y;
        TreeNode node;
        Tuple(int x,int y,TreeNode node){
            this.x=x;
            this.y=y;
            this.node=node;
        }
    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        Map<Integer,Map<Integer,ArrayList<Integer>>> map=new TreeMap<>();
        Queue<Tuple> q=new LinkedList<>();
        List<List<Integer>> ans=new ArrayList<>();

        q.add(new Tuple(0,0,root));
        while(!q.isEmpty()){
            Tuple ptr=q.remove();
            int h=ptr.x;
            int v=ptr.y;

            if(map.containsKey(v)){
                if(map.get(v).containsKey(h))
                   map.get(v).get(h).add(ptr.node.val);
                else{
                    ArrayList<Integer> temp=new ArrayList<>();
                    temp.add(ptr.node.val);
                    map.get(v).put(h,temp);
                }
            }
            else{
                map.put(v,new TreeMap<>());
                ArrayList<Integer> temp=new ArrayList<>();
                temp.add(ptr.node.val);
                map.get(v).put(h,temp);
            }

            if(ptr.node.left!=null) q.add(new Tuple(h+1,v-1,ptr.node.left));
            if(ptr.node.right!=null) q.add(new Tuple(h+1,v+1,ptr.node.right));
        }

        for(int i:map.keySet()){
            Map<Integer,ArrayList<Integer>> t=map.get(i);
            ArrayList<Integer> f=new ArrayList<>();
            for(int j:t.keySet()){
               ArrayList<Integer> a=t.get(j);
               Collections.sort(a);
               for(int k:a) f.add(k);
            }
            ans.add(f);
        }

        return ans;
    }
}