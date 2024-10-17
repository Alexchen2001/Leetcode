# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        targetNode1 = None
        val1 = None
        targetNode2 = None
        val2 = None
        count = 1
        while head:
            if count == k:
                targetNode1 = head
                val1 = head.val
            head = head.next
            count += 1
        
        count2 = count - k
        head = dummy.next
        print(count2)
        index = 1
        while head:
            if index == count2:
                targetNode2 = head
                val2 = head.val
            head = head.next
            index += 1
            
        targetNode1.val = val2
        targetNode2.val = val1

        return dummy.next
        
        
        
