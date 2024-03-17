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
    public ListNode reverseList(ListNode head) {
        ListNode ptr=head,pre=null,fut=null;
        while(ptr!=null){
            fut=ptr.next;
            ptr.next=pre;
            pre=ptr;
            ptr=fut;
        }
        return pre;
    }
}