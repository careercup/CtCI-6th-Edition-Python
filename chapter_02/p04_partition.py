from chapter_02.linked_list import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None
    return ll


def lr_partition(_ll: LinkedList, p: int) -> LinkedList:
    """
    Create 2 LinkedList (left and right), and return a combined LinkedList
    """
    left = LinkedList()
    right = LinkedList()

    current = _ll.head
    while current:
        if current.value < p:
            left.add(current.value)
        else:
            right.add(current.value)

        current = current.next

    left.tail.next = right.head
    return left


def test_lr_partition():
    partitioners = [partition, lr_partition]
    for partition_func in partitioners:
        # book example
        ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
        assert not is_partitioned(ll, x=5)
        ll = partition_func(ll, 5)
        assert is_partitioned(ll, x=5), f"{partition_func} did not partition {ll}"

        # random example
        ll = LinkedList.generate(10, 0, 99)
        x = ll.head.value
        ll = partition_func(ll, x)
        assert is_partitioned(ll, x=x), f"{partition_func} did not partition"


def is_partitioned(ll, x):
    seen_gt_partition = False
    for node in ll:
        if node.value >= x:
            seen_gt_partition = True
            continue
        if seen_gt_partition and node.value < x:
            return False
    return True


if __name__ == "__main__":
    test_lr_partition()
