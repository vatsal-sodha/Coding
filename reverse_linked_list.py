# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(self, head: ListNode) -> ListNode:
        currentNode = head
        prev = None
        while currentNode != None:
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
        return prev