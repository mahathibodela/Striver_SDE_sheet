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
    public boolean hasCycle(ListNode head) {
        ListNode f=head,s=head;
        int a=1;
        while(f!=null && s!=null){
            f=f.next;
            if(f!=null) f=f.next;
            s=s.next;
            if(f!=null && s!=null){
                if(f==s) return true;
            }
        }
        return false;
    }
}