class LRUCache {
    class Node{
        int key,val;
        Node pre,next;
        Node(int key,int val){
            this.val=val;
            this.key=key;
            pre=null;
            next=null;
        }
    }
    Node head=new Node(0,0);
    Node tail=new Node(0,0);

    int cap;
    Map<Integer,Node> map=new HashMap<>();

    public void insert(int key,int value){
        if(key==4)
           for(int i:map.keySet()) System.out.print(i+" ");
        Node node=new Node(key,value);
        node.next = head.next;
        node.next.pre = node;
        head.next = node;
        node.pre = head;
        map.put(key,node);
        if(key==4)
           for(int i:map.keySet()) System.out.print(i+" ");
    }
    
    public void  remove(Node ptr){
        map.remove(ptr.key);
        ptr.pre.next=ptr.next;
        ptr.next.pre=ptr.pre;
    }

    public LRUCache(int capacity) {
        cap=capacity;
        head.next=tail;
        tail.pre=head;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            Node ptr=map.get(key);
            int ke=ptr.val;
            ptr.pre.next=ptr.next;
            ptr.next.pre=ptr.pre;
            insert(key,ke);
            return ke;
        }
        else return -1;
    }
    
    public void put(int key, int value) {
        // System.out.println(key);
        // for(int i:map.keySet()) System.out.print(i+" ");
        // System.out.println(" ");
        if(map.size()<cap || map.containsKey(key)){
            if(map.containsKey(key))
               remove(map.get(key));
            insert(key,value);
        }
        else{
            // System.out.println(key+"here");
            remove(tail.pre);
            insert(key,value);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */