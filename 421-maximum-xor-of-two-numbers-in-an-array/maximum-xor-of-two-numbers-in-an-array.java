class Node{
    Node[] links=new Node[2];
    boolean isContains(int i){
        return (links[i]!=null);
    }
    void put(int i,Node node){
        links[i]=node;
    }
    Node get(int i){
        return links[i];
    }
}
class Trie{
    Node root;
    Trie(){
        root=new Node();
    }
    void insert(int num){
        Node temp=root;
        for(int i=31;i>=0;i--){
            int k = (num>>i) & 1;
            if(!temp.isContains(k)){
                temp.put(k,new Node());
            }
            temp=temp.get(k);
        }
    }
    int getMax(int num){
        int sum=0;
        Node temp=root;
        for(int i=31;i>=0;i--){
            int k = (num>>i) & 1;
            if(temp.isContains(1-k)){
               sum=sum | (1<<i);
               temp=temp.get(1-k);
            }else{
               temp=temp.get(k);
            }
        }
        return sum;
    }
}
class Solution {
    public int findMaximumXOR(int[] nums) {
        Trie trie=new Trie();
        int n=nums.length;

        for(int i=0;i<n;i++){
            trie.insert(nums[i]);
        }

        int ans=0;
        for(int i=0;i<n;i++){
            ans=Math.max(ans,trie.getMax(nums[i]));
        }

        return ans;
    }
}