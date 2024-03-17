class Solution {
    public String longestCommonPrefix(String[] strs) {
        //sort karsakthe ho hamesha think out of the box its
        //really necesary dont forget

        Arrays.sort(strs);
        int ind=Math.min(strs[0].length(),strs[strs.length-1].length());
        String f=strs[0];
        String l=strs[strs.length-1];
        int i=0,c=0;;
        while(i<ind){
            if(f.charAt(i)==l.charAt(i)){
               c++;
               i++;
            }
            else break;
        }

        return f.substring(0,c);
    }
}