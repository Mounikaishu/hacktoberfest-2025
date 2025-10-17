# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findKth(self, head: ListNode, k: int) -> ListNode:
        temp = head
        while temp and k > 1:
            k -= 1
            temp = temp.next
        return temp

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        temp = head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp = head
        prevNode = None
        new_head = head

        while temp:
            kthNode = self.findKth(temp, k)
            if not kthNode:
                if prevNode:
                    prevNode.next = temp
                break

            nextNode = kthNode.next
            kthNode.next = None
            self.reverseList(temp)

            if temp == head:
                new_head = kthNode
            else:
                prevNode.next = kthNode

            prevNode = temp
            temp = nextNode

        return new_head
