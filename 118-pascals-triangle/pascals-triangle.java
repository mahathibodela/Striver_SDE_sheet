class Solution {
    public List<List<Integer>> generate(int numRows) {
        int n=numRows;
        List<List<Integer>> a=new ArrayList<>();
        for(int i=0;i<n;i++){
            List<Integer> sa=new ArrayList<>();
            sa.add(1);
            for(int j=0;j<i-1;j++){
                sa.add(a.get(i-1).get(j)+a.get(i-1).get(j+1));
            }
            if(i!=0)
               sa.add(1);
            a.add(sa);
        }
        return a;
    }
}