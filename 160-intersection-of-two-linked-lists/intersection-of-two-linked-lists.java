/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> s=new HashSet<>();
        ListNode ptr=null;
        while(headA!=null && headB!=null){
            if(s.contains(headA))
              return headA;
            else s.add(headA);
            if(s.contains(headB))
              return headB;
            else s.add(headB);

            headA=headA.next;
            headB=headB.next;
        }
        if(headA!=null) ptr=headA;
        if(headB!=null) ptr=headB;

        while(ptr!=null){
           if(s.contains(ptr))
              return ptr;
            else s.add(ptr);
            ptr=ptr.next;
        }

        return null;
    }
}