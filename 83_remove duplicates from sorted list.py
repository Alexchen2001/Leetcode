# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## pass by reference
        ## initiate a temp pointer node
        currNode = head
        
        ## only iterates if there is a node and a next node available
        while currNode and currNode.next:
            
            ## if value matches, then points the next of the current node to the one after
            if (currNode.val == currNode.next.val):
                currNode.next = currNode.next.next
            ## otherwise remain the same
            else:
                currNode = currNode.next
        
        ## return back the linked list
        return head
        