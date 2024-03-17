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
class sortBy implements Comparator<ArrayList<Integer>>{
    public int compare(ArrayList<Integer> a,ArrayList<Integer> b){
        return a.get(0).compareTo(b.get(0));
    }
}
class Solution {
    public int[] maximizeXor(int[] nums, int[][] queries) {
        Arrays.sort(nums);

        ArrayList<ArrayList<Integer>> data=new ArrayList<>();
        int n=queries.length;

        for(int i=0;i<n;i++){
            ArrayList<Integer> a=new ArrayList<>();
            a.add(queries[i][1]);
            a.add(queries[i][0]);
            a.add(i);
            data.add(a);
        }
        Collections.sort(data,new sortBy());

        Trie trie=new Trie();
        int ind=0;
        int[] ans=new int[n];
        int numsL=nums.length;

        for(int i=0;i<n;i++){
            int ai=data.get(i).get(0);
            int xi=data.get(i).get(1);
            int pi=data.get(i).get(2);
            while(ind<numsL && nums[ind]<=ai){
                trie.insert(nums[ind]);
                ind++;
            }
            if(ind==0) ans[pi]=-1;
            else ans[pi]=trie.getMax(xi);      
        }

        return ans;
    }
}