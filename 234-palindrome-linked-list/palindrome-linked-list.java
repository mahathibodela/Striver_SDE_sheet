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
    public boolean isPalindrome(ListNode head) {
        ListNode s=head,f=head;
        while(f.next!=null && f.next.next!=null){
            s=s.next;
            f=f.next.next;
        }
        
        ListNode ptr=s.next,pre=null,fut=null;
        while(ptr!=null){
            fut=ptr.next;
            ptr.next=pre;
            pre=ptr;
            ptr=fut;
        }

        ListNode temp=pre;
        //if(temp==null) return false;
        //System.out.println(temp.val+" "+head.val);
        while(head!=temp && temp!=null){
            if(head.val==temp.val){
                head=head.next;
                temp=temp.next;
            }
            else return false;
        }

        return true;
    }
}