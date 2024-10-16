# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        res = None
        while (l1 or l2) or rem > 0:
            if l1 is None:
                temp1 = 0
            else: 
                temp1 = l1.val
            if l2 is None:
                temp2 = 0
            else:
                temp2 = l2.val
            

            sum = temp1 + temp2 + rem
            rem = sum // 10
            temp = res
            res = ListNode(val = (sum % 10), next = temp)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        head = res
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev



            