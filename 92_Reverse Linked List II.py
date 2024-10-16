# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        currNode = head
        index = 1
        leftNode= None
        rightNode= None
        # Node before left
        # Node after right
        NodeLeft = None
        NodeRight = None
        prevNode = None
        while currNode:
            if index == left:
                leftNode = currNode
                NodeLeft = prevNode
            if index == right:
                rightNode = currNode
                NodeRight = currNode.next
                break
            index += 1
            prevNode = currNode
            currNode = currNode.next

        reverseHead = leftNode
        reversePrev = None
        index = left
        while reverseHead and (index < right + 1):
            reverseNext = reverseHead.next
            reverseHead.next = reversePrev
            reversePrev = reverseHead
            reverseHead = reverseNext
            index += 1
        
        leftNode.next = NodeRight
        if NodeLeft is None:
            return rightNode
        NodeLeft.next = rightNode



        return head
                
            

            

