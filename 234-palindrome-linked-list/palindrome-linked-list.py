# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num = ''
        while head:
            num = num + str(head.val)
            head = head.next
        return num == num[::-1]

        