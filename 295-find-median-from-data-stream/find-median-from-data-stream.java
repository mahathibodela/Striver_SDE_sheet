class minsort implements Comparator<Integer>{
    public int compare(Integer a,Integer b){
        if(b>a) return 1;
        else if(b==a) return 0;
        return -1;
    }
}
class maxsort implements Comparator<Integer>{
    public int compare(Integer a,Integer b){
        if(b<a) return 1;
        else if(b==a) return 0;
        return -1;
    }
}
class MedianFinder {
    Queue<Integer> minQueue=new PriorityQueue<>(new maxsort());  
    Queue<Integer> maxQueue=new PriorityQueue<>(new minsort());
    int n=0;
    void rearrange(Queue<Integer> minQueue,Queue<Integer> maxQueue){
     if(!minQueue.isEmpty() && !maxQueue.isEmpty() && maxQueue.peek()>minQueue.peek())
     {
        minQueue.add(maxQueue.remove());
     }
     if(minQueue.size()>maxQueue.size()+1){
        maxQueue.add(minQueue.remove());
     }
     else if(minQueue.size()+1<maxQueue.size()){
        minQueue.add(maxQueue.remove());
     }
    }
    public MedianFinder() {

    }
    
    public void addNum(int num) {
        n++;
        maxQueue.add(num);
        rearrange(minQueue,maxQueue);
    }
    
    public double findMedian() {
        if(n%2!=0){
            if(minQueue.size()>maxQueue.size()){
                return minQueue.peek();
            }
            return maxQueue.peek();
        }
        double a=maxQueue.peek();
        double b=minQueue.peek();
        return (a+b)/2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */