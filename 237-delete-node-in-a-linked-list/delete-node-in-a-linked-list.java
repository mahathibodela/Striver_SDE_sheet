/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        ListNode ptr=node.next;

        while(ptr!=null){
            node.val=ptr.val;
            node.next=ptr.next;
            ptr=ptr.next;
            node=node.next;
        }
        // node.val=ptr.val;
        // node.next=ptr.next;
        
    }
}