class Solution {
    public int[][] merge(int[][] intervals) {

    //yaha sorting bahut asani se kiya gaya bey...c++ main hain just arr.sort(arr.begin())
        // arr.ennd()  bekar ka lika tum itna zyada
        TreeMap<Integer,List> map=new TreeMap<Integer,List>();
        for(int i=0;i<intervals.length;i++){
            if(map.containsKey(intervals[i][0]))
               map.get(intervals[i][0]).add(i);
            else{
                List<Integer> a=new LinkedList<>();
                a.add(i);
                map.put(intervals[i][0],a);
            }
        }
        Set<Integer> c=map.keySet();
        List<List<Integer>> a=new LinkedList<>();
        for(Integer z:c){
            List<Integer> l=map.get(z);
            for(int i=0;i<l.size();i++){
                List<Integer> sa=new LinkedList<>();
                int m=l.get(i);
                sa.add(intervals[m][0]);
                sa.add(intervals[m][1]);
                a.add(sa);    
            }
        }
        for(int i=1;i<a.size();i++){
            if((a.get(i).get(0)<=a.get(i-1).get(1)) &&(a.get(i).get(1)<=a.get(i-1).get(1)))           {
                a.remove(i);
                i=i-1;
             }
            else if((a.get(i).get(0)<=a.get(i-1).get(1))){
                a.get(i).set(0,a.get(i-1).get(0));
                a.remove(i-1);
                i=i-1;
            }
        }
        
        int s=a.size();
        int[][] m=new int[s][2];
        for(int i=0;i<s;i++){
            for(int j=0;j<2;j++){
                m[i][j]=a.get(i).get(j);
            }
        }
        
        return m;
    }
}