# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set()
        itr=head
        cycleFound=False
        index=0
        while itr and itr.next is not None:
            if itr not in seen:
                seen.add(itr)           
            else:
                return True
            itr=itr.next
        return False   

        