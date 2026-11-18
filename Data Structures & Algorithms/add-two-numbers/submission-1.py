# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        head=dummy
        carry=0
        while l1 or l2:
            if l2 is None:
                val2=0
            else:
                val2=l2.val
                l2=l2.next
            if l1 is None:
                val1=0
            else:
                val1=l1.val
                l1=l1.next

            sum=val1+val2+carry
            val=sum%10
            carry=sum//10
            dummy.next=ListNode(val,None)
            dummy=dummy.next

        if carry !=0:
            dummy.next=ListNode(carry)
        
        return head.next