class Solution {
    boolean isPalin(String s){
        if(s.length()==1 || s.length()==0) return true;
            
        if(s.charAt(0)==s.charAt(s.length()-1))
            return isPalin(s.substring(1,s.length()-1));
        else 
            return false;
    }
    void check(int i,String s,List<List<String>> ans,List<String> a){
        if(i==s.length()){
            ans.add(new ArrayList<>(a));
            return ;
        }

        for(int j=i+1;j<=s.length();j++){
            if(isPalin(s.substring(i,j))){
                a.add(s.substring(i,j));
                check(j,s,ans,a);
                a.remove(a.size()-1);
            }
        }
    }
    public List<List<String>> partition(String s) {
        List<List<String>> ans=new ArrayList<>();
        List<String> a=new ArrayList<>();
        check(0,s,ans,a);
        return ans;
    }
}