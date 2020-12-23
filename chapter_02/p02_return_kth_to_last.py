from chapter_02.linked_list import LinkedList


def kth_to_last(ll, k):
    runner = current = ll.head
    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
