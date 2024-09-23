# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pointer = head
        while pointer:
            if pointer.next and pointer.next.val == pointer.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head


        
