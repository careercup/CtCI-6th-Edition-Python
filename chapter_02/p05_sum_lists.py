from chapter_02.linked_list import LinkedList
import pytest


def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = NumericLinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll


def sum_lists_recursive(ll1, ll2) -> LinkedList:
    def sum_lists_helper(ll1_head, ll2_head, remainder, summed_list):
        if ll1_head is None and ll2_head is None:
            if remainder != 0:
                summed_list.add(remainder)
            return summed_list
        elif ll1_head is None:
            result = ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head, ll2_head.next, result//10, summed_list)
        elif ll2_head is None:
            result = ll1_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head.next, ll2_head, result//10, summed_list)
        else:
            result = ll1_head.value + ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head.next, ll2_head.next, result//10, summed_list)     
    return sum_lists_helper(ll1.head, ll2.head, 0, LinkedList())


# this solution does not pass tests
# def sum_lists_followup(ll_a, ll_b):
#     # Pad the shorter list with zeros
#     if len(ll_a) < len(ll_b):
#         for i in range(len(ll_b) - len(ll_a)):
#             ll_a.add_to_beginning(0)
#     else:
#         for i in range(len(ll_a) - len(ll_b)):
#             ll_b.add_to_beginning(0)
#
#     # Find sum
#     n1, n2 = ll_a.head, ll_b.head
#     result = 0
#     while n1 and n2:
#         result = (result * 10) + n1.value + n2.value
#         n1 = n1.next
#         n2 = n2.next
#
#     # Create new linked list
#     return NumericLinkedList([int(i) for i in str(result)])


class NumericLinkedList(LinkedList):
    @classmethod
    def generate_from_integer(cls, integer):
        integer_parts = [int(c) for c in str(integer)]
        integer_parts.reverse()
        return cls(integer_parts)

    def numeric_value(self):
        number = 0
        for place, node in enumerate(self):
            number += node.value * 10**place
        return number


test_cases = (
    # all values can either be list of integer or integers
    # a, b, expected_sum
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    (0, 0, 0),
    ([], [], 0),
    ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    (123, 123, 246),
    (123, 1, 124),
    (1, 123, 124),
)

testable_functions = (
    sum_lists,
    # sum_lists_followup
)


def test_numeric_linked_list():
    ll = NumericLinkedList.generate_from_integer(321)
    assert ll.numeric_value() == 321


def test_linked_list_addition():
    for f in testable_functions:
        for a, b, expected in test_cases:
            print(f"{f.__name__}: {a}, {b}, {expected}")
            if isinstance(a, int):
                ll_a = NumericLinkedList.generate_from_integer(a)
            else:
                ll_a = NumericLinkedList(a.copy())

            if isinstance(b, int):
                ll_b = NumericLinkedList.generate_from_integer(b)
            else:
                ll_b = NumericLinkedList(b.copy())
            result = f(ll_a, ll_b)
            if isinstance(expected, int):
                assert result.numeric_value() == expected
            else:
                assert result.values() == expected


def example():
    ll_a = LinkedList.generate(4, 0, 9)
    ll_b = LinkedList.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(sum_lists(ll_a, ll_b))
    # print(sum_lists_followup(ll_a, ll_b))


class TestSumListsRecursive:
    def test_empty(self):
        assert sum_lists_recursive(LinkedList(), LinkedList()).values() == LinkedList().values()
    
    def test_single_digit(self):
        assert sum_lists_recursive(LinkedList([1]), LinkedList([2])).values() == LinkedList([3]).values()
    
    def test_ll1_longer(self):
        assert sum_lists_recursive(LinkedList([1, 2]), LinkedList([2])).values() == LinkedList([3, 2]).values()
    
    def test_ll2_longer(self):
        assert sum_lists_recursive(LinkedList([2]), LinkedList([1, 2])).values() == LinkedList([3, 2]).values()
    
    def test_carry_end(self):
        assert sum_lists_recursive(LinkedList([9, 9, 9]), LinkedList([1, 0, 0])).values() == LinkedList([0, 0, 0, 1]).values()
    
    def test_multiple_carry(self):
        assert sum_lists_recursive(LinkedList([9, 9, 9]), LinkedList([9, 9, 9])).values() == LinkedList([8, 9, 9, 1]).values()


if __name__ == "__main__":
    example()
    pytest.main(args=[__file__])
