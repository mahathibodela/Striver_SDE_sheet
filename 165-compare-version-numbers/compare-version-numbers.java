class Solution {
    public int compareVersion(String version1, String version2) {
        int n=version1.length(),m=version2.length();
        int i=0,j=0;

        while(i<n || j<m){
            int n1=0;
            int n2=0;
            while(i<n && version1.charAt(i)!='.'){
                n1=n1*(10)+(version1.charAt(i)-'0');
                i++;
            }
            while(j<m && version2.charAt(j)!='.'){
                n2=n2*(10)+(version2.charAt(j)-'0');
                j++;
            }
            if(n1<n2) return -1;
            else if(n1>n2) return 1;
            i++;j++;
        }

        return 0;
    }
}