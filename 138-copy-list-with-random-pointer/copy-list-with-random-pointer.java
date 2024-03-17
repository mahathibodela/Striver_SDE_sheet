/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return null;
        //step -1
        Node ptr=head;
        while(ptr!=null){
            Node temp=new Node(ptr.val);
            temp.next=ptr.next;
            ptr.next=temp;
            ptr=ptr.next.next;
        }
        //ab random pointer
        ptr=head;
        while(ptr!=null){
            if(ptr.random!=null)
             ptr.next.random=ptr.random.next;
            ptr=ptr.next.next;
        }
        //divide karo ab
        ptr=head;
        Node f=head.next.next;
        Node head1=head.next;
        while(ptr!=null){
            if(f==null){
                ptr.next.next=null;
                ptr.next=null;
                break;
            }
            ptr.next.next=f.next;
            ptr.next=f;
            ptr=f;
            f=ptr.next.next;
        }

        return head1;
    }
}