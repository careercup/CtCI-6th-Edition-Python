from LinkedList import LinkedList


def is_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True


def is_palindrome_big_O_of_one_space(ll):
    """
    Improves on the current solution by
    using less (constant) space (O(N) --> O(1)).
    """
    # find the list center via the runner technique
    slow = ll.head
    fast = slow.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # unlink left and right halves of the list
    right_head = slow.next
    slow.next_node = None
    # reverse the right half of the list
    tail = reverse(right_head)
    # iterate over nodes from the outside in
    left, right = ll.head, tail
    result = True
    while left and right:
        if left.value != right.value:
            result = False
            break
        left = left.next
        right = right.next
    # undo state changes
    reverse(tail)
    slow.next_node = right_head
    return result


def reverse(node):
    """
    reverses a linked list,
    returns the input list's
    tail node as the new head

        Time : O(N)
        Space: O(1)
    """
    previous_node = None
    while node:
        # keep track of the next node
        next_node = node.next
        # point the current node backwards
        node.next = previous_node
        # advance pointers
        previous_node = node
        node = next_node
    return previous_node


ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
print(is_palindrome_big_O_of_one_space(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
print(is_palindrome_big_O_of_one_space(ll_false))

