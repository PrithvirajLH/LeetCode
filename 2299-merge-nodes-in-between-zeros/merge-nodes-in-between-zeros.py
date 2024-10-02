# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        second = first.next

        value = 0
        while second:
            if second.val != 0:
                value += second.val
                second = second.next
            else:
                new = ListNode(value)
                first.next = new
                new.next = second
                first = new
                second = second.next
                value = 0
        first.next = None
        return head.next


