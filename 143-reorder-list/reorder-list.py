# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        forw = None

        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
        
        first = head
        second = prev
        temp = head

        while second.next:
            temp = temp.next
            first.next = second
            second = second.next
            first.next.next = temp
            first = first.next.next
        
        return head

