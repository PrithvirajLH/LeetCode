# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0

        while temp:
            temp = temp.next
            count += 1
        middle = count // 2

        for i in range(middle):
            head = head.next 
        return head
         

        