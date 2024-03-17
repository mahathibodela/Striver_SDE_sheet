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
    public ListNode removeNthFromEnd(ListNode head, int n) {
      ListNode d1=null,d2=null;
      for(int i=0;i<n;i++){
          if(d1==null)
            d1=head;
          else
            d1=d1.next;
      }
      ListNode ans=null;
      while(d1.next!=null){
          if(d2==null){
             d2=head;
             ans=d2;
          }
          else
            d2=d2.next;
          d1=d1.next;
      }
      //YEHI PAI TUMKO BORDER CASE SOCHNA PADEGA U R MISSING IT SAVADHAN
      if(d2==null){
          ans=head.next;
          return ans;
      }
      d2.next=d2.next.next;
      return ans ;   
    }
}