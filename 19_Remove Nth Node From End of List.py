# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currNode = head
        prevNode = None
        nextNode = head.next
        index = 1
        while nextNode:
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
            index += 1
        
        targetIndex = index - n
        i = 1
        currNode = head
        prevNode = None
        nextNode = head.next
        while nextNode and i <= targetIndex:
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
            i += 1
        if prevNode:
            prevNode.next = nextNode
        elif nextNode:
            return nextNode
        else:
            return prevNode

        return head