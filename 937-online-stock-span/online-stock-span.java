class StockSpanner {

    ArrayList<Integer> no=new ArrayList<>();
    ArrayList<Integer> hi=new ArrayList<>();
    public StockSpanner() {
        
    }
    
    public int next(int price) {
        int s=no.size();
        no.add(price);
        if(s==0){
          hi.add(-1);
          return 1;
        }
        else if(no.get(s-1)>price){
            hi.add(s-1);
            return 1;
        }
        else{
            int c=1;
            int i=s-1;
            while(no.get(i)<=price){   
                c=c+1;
                i=hi.get(i);
                if(i==-1) break;
            }
            hi.add(i);
            return s-i;
        }
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */