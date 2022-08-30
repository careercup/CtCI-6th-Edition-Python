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


def lr_partition(_ll: LinkedList, p: int) -> LinkedList:
    '''
    Create 2 LinkedList (left and right), and return a combined LinkedList
    '''
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


def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    partition(ll, ll.head.value)
    print(ll)

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    ll = lr_partition(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    example()
