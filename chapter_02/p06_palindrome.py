from .linked_list import LinkedList


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


def test_is_palindrome():
    ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
    assert is_palindrome(ll_true)
    ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert not is_palindrome(ll_false)
