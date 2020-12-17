import time

from chapter_02.linked_list import LinkedList


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


def is_palindrome_constant_space(ll):
    """
    Constant(O(1)) space solution
    """
    # find the list center via the runner technique
    slow = ll.head
    if not slow or not slow.next:
        return True

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


test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
]

testable_functions = [is_palindrome, is_palindrome_constant_space]


def test_is_palindrome():
    for f in testable_functions:
        start = time.perf_counter()
        for values, expected in test_cases:
            print(f"{f.__name__}: {values}")
            for _ in range(100):
                assert f(LinkedList(values)) == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    test_is_palindrome()
