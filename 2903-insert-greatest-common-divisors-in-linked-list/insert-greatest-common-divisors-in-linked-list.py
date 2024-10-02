# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = first.next

        while second:
            small = min(first.val, second.val)
            while small > 0:
                if first.val % small == 0 and second.val % small == 0:
                    break
                else:
                    small -= 1
            new = ListNode(small)
            first.next = new
            new.next = second
            first = second
            second = second.next
        return head

        