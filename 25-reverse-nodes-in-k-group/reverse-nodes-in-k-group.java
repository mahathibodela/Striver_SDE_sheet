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
    public ListNode reverseKGroup(ListNode head, int k) {
        //EDGE CASES PURA CHOD DIYA TUMNE
        //K==1 HEADD==NULL BREAK WALLA CHODA
        //IF IT IS PERFECT MULTIPLE CHODA
        //BEKAR HO
        if(k==1) return head;
        ListNode start=null,end=null,ptr=null,pre=null,fut=null,temp=head,ans=null,p=null;
        ListNode headd=null;
        while(temp!=null){
            start=temp;
            for(int i=0;i<k;i++){
                if(temp!=null)
                  temp=temp.next;
                else{
                 if(headd==null) break;
                 ans.next=start;
                 return headd;
                }
            }
            end=temp;
            ptr=start;
            while(ptr!=end){
                fut=ptr.next;
                ptr.next=pre;
                pre=ptr;
                ptr=fut;
            }
            if(headd==null){
               headd=pre;
               ans=start;
            }
            else{
               ans.next=pre;
                ans=start;
            }
        }
        ans.next=null;
        return headd;
    }
}