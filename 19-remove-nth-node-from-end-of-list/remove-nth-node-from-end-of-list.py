# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        prev = reverse(head)
        second = prev

        if n == 1:
            prev = second.next
        else:
            count = 1
            while count != n - 1:
                second = second.next
                count  += 1
            second.next = second.next.next


        return reverse(prev)
        
        
            

        