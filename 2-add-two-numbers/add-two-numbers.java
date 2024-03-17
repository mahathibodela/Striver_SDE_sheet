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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans=null,nextt=null,ptr=null;
        int sum=0,c=0,f=1;

       //EDGE CASES BAHUT MISS KARAEHHO
       //CAN DIRECTLY WRITE KI SAB JAHA TAK HONGE TAK TAK
        while(l1!=null && l2!=null){
            sum=l1.val+l2.val+c;
            l1=l1.next;
            l2=l2.next;
            c=sum/10;
            ListNode temp=new ListNode(sum%10);
            temp.next=null;
            if(f==1){
              ans=temp;
              ptr=ans;
            }
            else{
              ptr.next=temp; 
              ptr=temp;
            }
            f=f+1;
        }

        if(l1!=null) nextt=l1;
        else nextt=l2;

        if(nextt==null){
            if(c!=0){
            ListNode temp=new ListNode(c);
            ptr.next=temp; 
            }
        }
        else{
            while(c!=0 || nextt!=null){
                sum=c;
                if(nextt!=null){
                  sum=sum+nextt.val;
                  nextt=nextt.next;
                }
                c=sum/10;
                ListNode temp=new ListNode(sum%10);
                ptr.next=temp;
                ptr=temp; 
            }
        }

        return ans;
    }
}