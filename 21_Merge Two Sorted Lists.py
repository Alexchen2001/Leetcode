# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0,None)
        dummy = ListNode(0,head)
        
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    head.next = list1
                    list1 = list1.next
                    head = head.next
                else:
                    head.next = list2
                    list2 = list2.next
                    head = head.next
            elif list1 and not list2:
                head.next = list1
                break
            elif list2 and not list1:
                head.next = list2
                break
        return dummy.next.next
