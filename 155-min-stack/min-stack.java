class Pair{
    int x,y;
    Pair(int x,int y){
        this.x=x;
        this.y=y;
    }
}
class MinStack {
    Stack<Pair> s;
    public MinStack() {
        s=new Stack<>();
    }
    
    public void push(int val) {
        if(s.size()==0) s.push(new Pair(val,val));
        else{
            Pair temp=s.peek();
            s.push(new Pair(val,Math.min(val,temp.y)));
        }
    }
    
    public void pop() {
        Pair p=s.pop();
    }
    
    public int top() {
        Pair p=s.peek();
        return p.x;
    }
    
    public int getMin() {
        Pair p=s.peek();
        return p.y;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */