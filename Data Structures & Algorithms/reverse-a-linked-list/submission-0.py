# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        stack=[]
        while itr !=None:
            stack.append(itr)
            itr=itr.next
        itr=ListNode()
        new_head=itr

        while len(stack)>0:
            elem=stack.pop()
            print(elem.val)
            elem.next=None
            itr.next=elem
            itr=itr.next
            
        return new_head.next