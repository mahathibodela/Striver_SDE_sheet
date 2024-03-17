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
    public ListNode middleNode(ListNode head) {
        ListNode ft=head,st=head;
        while(ft!=null ||ft.next==null){
            ft=ft.next;
            if(ft!=null){
            ft=ft.next;
            st=st.next;
            }
            if(ft==null ||ft.next==null)
              return st;
        }
        return st;
    }
}