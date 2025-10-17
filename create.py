# Helper to create a linked list
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper to print linked list
def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# Example
l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])
sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print_list(result)  # Output: [7, 0, 8]
