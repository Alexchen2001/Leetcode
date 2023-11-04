# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ## checks for the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        ## iterates to the linked list to obtain the node desired.
        aim = length // 2   
        result = head
        for i in range (aim):
            result = result.next
        
        return result
        
            
        