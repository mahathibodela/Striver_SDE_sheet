/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode f=head,s=head;
        int c=1;
        if(f==null || f.next==null) return null;
        if(f.next!=null && f.next.next!=null && f.next.next==f) return f;

        do{
            if(f==null) return null;
            f=f.next;
            if(f==null) return null;
            f=f.next;
            s=s.next;
            if(s==null) return null;
        }while(f!=s);

        while(head!=s){
            head=head.next;
            s=s.next;
        }
        
        return s;
       
        
    }
}