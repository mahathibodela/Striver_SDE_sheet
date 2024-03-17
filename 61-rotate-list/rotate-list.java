/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null) return null;
        if(k==0) return head;
        ListNode temp=head,ptr=head,nh=null;
        int c=1;
        for(int i=0;i<k;i++) {
            temp=temp.next;
            if(temp==null){
                temp=head;
                if(c==k || (k%c==0)) return head;
                else {
                    for(int j=0;j<(k%c);j++) temp=temp.next;
                    break;
                }
            }
            c=c+1;
        }
        while(temp.next!=null){
            ptr=ptr.next;
            temp=temp.next;
        }
        nh=ptr.next;
        ptr.next=null;
        temp=nh;
        while(temp.next!=null) temp=temp.next;
        temp.next=head;
        return nh;
    }
}