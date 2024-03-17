class Solution {
    public int myAtoi(String s) {
        int l=0,n=s.length(),ne=0;
        double ans=0,max=Integer.MAX_VALUE,min=Integer.MIN_VALUE;
        
        if(n==0) return 0;
        int i=0;
        if(s.charAt(i)==' '){
            while(i<n && s.charAt(i)==' ') i++;
        }
        if(i<n && s.charAt(i)=='-'){
            ne=1;
            i++;
        }
        else if(i<n && s.charAt(i)=='+'){
            i++;
        }
        if(i<n && s.charAt(i)=='0'){
            while(i<n && s.charAt(i)=='0'){
                i++;
            }
        }
        
        l=i;
        double temp=0;
        for(;i<n;i++){
            char c=s.charAt(i);
            if(!('0'<=c && c<='9')){
                break;
            }
            else{
                temp=Double.parseDouble(s.substring(l,i+1));
                if(ne==1) temp=temp*(-1);
                System.out.println(temp+" "+min);
                if(temp<min) return (int)min;
                if(temp>max){
                  System.out.println("here");
                  return (int)max;
                }
            }
        }
        
        
        
        return (int)temp;
        
    }
}