# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextNode = None
        prevNode = head
        while head:
            prevNode = head.next
            head.next = nextNode
            nextNode = head
            head = prevNode
        return nextNode