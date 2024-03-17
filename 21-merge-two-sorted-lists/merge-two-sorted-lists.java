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
    //BASE CASES DYAN NEHI DERAHHEO DENA HE
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head=null,temp=null,ptr1=list1,ptr2=list2;
        if(ptr1==null && ptr2==null) return null;
        if(ptr1==null && ptr2!=null) return ptr2;
        if(ptr1!=null && ptr2==null) return ptr1;
        if(list1.val<=list2.val){
             head=list1;
             ptr1=ptr1.next;
        }
        else {
            head=list2;
            ptr2=ptr2.next;
        }
        
        temp=head;
        while(ptr1!=null && ptr2!=null){
            if(ptr1.val<=ptr2.val){
              temp.next=ptr1;
              temp=ptr1;
              ptr1=ptr1.next;
            }
            else{
              temp.next=ptr2;
              temp=ptr2;
              ptr2=ptr2.next;
            }
        }
        if(ptr2!=null) temp.next=ptr2;
        else if(ptr1!=null) temp.next=ptr1;
        return head;
    }
}