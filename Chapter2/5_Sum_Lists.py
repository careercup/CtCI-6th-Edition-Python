from LinkedList import LinkedList


def sum_lists(ll_a, ll_b):
    a_val =0
    b_val = 0
    node_num = 0
    n1, n2 = ll_a.head, ll_b.head
    while n1:
        a_val = a_val + n1.value*(10**node_num)
        n1 = n1.next
        node_num+=node_num
    node_num = 0
    while n2:
        b_val = b_val+ n2.value*(10**node_num)
        n2 = n2.next
        node_num+=node_num
    result = a_val+b_val
    # Create new linked list
    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])

    return ll


ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))
