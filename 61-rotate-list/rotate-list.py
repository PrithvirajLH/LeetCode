# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        last = head
        n = 1
        while last.next:
            last = last.next
            n += 1
        
        last.next = head
        k = k % n

        for _ in range(n - k - 1):
            head = head.next
        
        answer = head.next
        head.next = None
        
        return answer
        
         

            

        