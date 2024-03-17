class Solution {
    public int strStr(String haystack, String needle) {
        //string matching henaa mujhe pata hain...
        int newl=haystack.length(),bn=needle.length();
        int i=-1;
         for( i=0;i<=(newl-bn);i++){
            if(haystack.regionMatches(i,needle,0,bn)){
                return i;
            }
        }
        return -1;
    }
}