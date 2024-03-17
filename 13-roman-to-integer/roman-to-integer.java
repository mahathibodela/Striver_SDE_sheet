class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> map=new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        int sum=0;
        int n=s.length();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='I'){
                if(i+1!=n && (s.charAt(i+1)=='V' || s.charAt(i+1)=='X'))
                    sum=sum-map.get('I');
                else
                    sum=sum+map.get('I');
            }
            else if(s.charAt(i)=='X'){
                if(i+1!=n && (s.charAt(i+1)=='L' || s.charAt(i+1)=='C'))
                    sum=sum-map.get('X');
                else
                    sum=sum+map.get('X');
            }
            else if(s.charAt(i)=='C'){
                if(i+1!=n && (s.charAt(i+1)=='D' || s.charAt(i+1)=='M'))
                    sum=sum-map.get('C');
                else
                    sum=sum+map.get('C');
            }
            else sum=sum+map.get(s.charAt(i));
        }

        return sum;
    }
}