# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        res = dummy
        prev = head
        curr = head.next

        while curr:
            if prev.val == curr.val:
                while curr and prev.val == curr.val:
                    curr = curr.next
                prev = curr
                if curr:
                    curr = curr.next
            else:
                dummy.next = prev
                prev = prev.next
                curr = curr.next
                dummy = dummy.next
        dummy.next = prev
        return res.next


            
            

        