class Solution {
    String check(int i,String s,int n){
        if(i==n) return s;
        int count=0,ni=s.length();
        char pre=' ';
        String ans="";

        for(int j=0;j<ni;j++){
            char c=s.charAt(j);
            if(c!=pre){
                if(count!=0){
                    String cc=Integer.toString(count);
                    ans=ans+cc+pre;
                }
                pre=c;
                count=1;
            }
            else count++;
        }
        String cc=Integer.toString(count);
        ans=ans+cc+pre;

        return check(i+1,ans,n);
    }
    public String countAndSay(int n) {
        return check(1,"1",n);
    }
}