from chapter_02.linked_list import LinkedList


def kth_to_last(ll, k):
    leader = follower = ll.head
    count = 0

    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = leader.next
    return follower


# O(N) space
def kth_last_recursive(ll, k):
    head = ll.head
    counter = 0

    def helper(head, k):
        nonlocal counter
        if not head:
            return None
        helper_node = helper(head.next, k)
        counter = counter + 1
        if counter == k:
            return head
        return helper_node

    return helper(head, k)


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        assert kth_last_recursive(ll, k).value == expected


if __name__ == "__main__":
    test_kth_to_last()
