# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(0,head)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = None
        while slow:
            temp = slow.next
            slow.next = second
            second = slow
            slow = temp
        maxNumber = 0
        while second:
            maxNumber = max(maxNumber, second.val + head.val)
            second = second.next
            head = head.next
        
        return maxNumber

