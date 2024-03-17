class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        // int ans=0;
        // for(int i=0;i<s.length();i++){
        //     Set<Character> set=new HashSet<>();
        //     for(int j=i;j<s.length();j++){
        //         if(set.contains(s.charAt(j)))
        //            break;
        //         set.add(s.charAt(j));
        //     }
        //     ans=Math.max(ans,set.size());
        //     if(s.length()-i-1==ans) return ans;
        // }
        Map<Character,Integer> map=new HashMap<>();
        int ans=0,si=0;
        for(int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
               si=Math.max(map.get(s.charAt(i))+1,si);
            }
            System.out.println(si+" "+i);
            map.put(s.charAt(i),i);
            ans=Math.max(ans,i-si+1);
        }

        return ans;
    }
}