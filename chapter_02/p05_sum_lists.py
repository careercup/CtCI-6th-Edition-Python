import pytest

from chapter_02.linked_list import LinkedList


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


def sum_lists_recursive(ll_a, ll_b) -> "NumericLinkedList":
    def sum_lists_helper(ll1_head, ll2_head, remainder, summed_list):
        if ll1_head is None and ll2_head is None:
            if remainder != 0:
                summed_list.add(remainder)
            return summed_list
        elif ll1_head is None:
            result = ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head, ll2_head.next, result // 10, summed_list)
        elif ll2_head is None:
            result = ll1_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(ll1_head.next, ll2_head, result // 10, summed_list)
        else:
            result = ll1_head.value + ll2_head.value + remainder
            summed_list.add(result % 10)
            return sum_lists_helper(
                ll1_head.next, ll2_head.next, result // 10, summed_list
            )

    return sum_lists_helper(ll_a.head, ll_b.head, 0, NumericLinkedList())


class NumericLinkedList(LinkedList):
    def __init__(self, values=None):
        """handle integer as input"""
        if isinstance(values, int):
            values = [int(c) for c in str(values)]
            values.reverse()
        elif isinstance(values, list):
            values = values.copy()

        super().__init__(values)

    def numeric_value(self):
        number = 0
        for place, node in enumerate(self):
            number += node.value * 10**place
        return number


def test_numeric_linked_list():
    ll = NumericLinkedList(321)
    assert ll.numeric_value() == 321
    assert ll.values() == [1, 2, 3]


testable_functions = (sum_lists, sum_lists_recursive)


@pytest.fixture(params=testable_functions)
def linked_list_summing_function(request):
    return request.param


test_cases = (
    # inputs can either be list of integer or integers
    # a, b, expected_sum
    pytest.param([1], [2], [3], id="single_digit"),
    pytest.param([0], [0], [0], id="single_digit_zero"),
    pytest.param([], [], [], id="empty"),
    pytest.param([7, 1, 6], [5, 9, 2], [2, 1, 9], id="3-digit equal length A"),
    pytest.param([3, 2, 1], [3, 2, 1], [6, 4, 2], id="3-digit equal length B"),
    pytest.param(123, 1, [4, 2, 1], id="3-digit and single digit"),
    pytest.param([9, 9, 9], [1], [0, 0, 0, 1], id="carry end"),
    pytest.param([9, 9, 9], [9, 9, 9], [8, 9, 9, 1], id="multiple carry"),
)


@pytest.mark.parametrize("a, b, expected", test_cases)
def test_linked_list_addition(linked_list_summing_function, a, b, expected):
    ll_a = NumericLinkedList(a)
    ll_b = NumericLinkedList(b)
    ll_result = linked_list_summing_function(ll_a, ll_b)
    assert ll_result.values() == expected
    assert (
        ll_a.numeric_value() + ll_b.numeric_value()
        == NumericLinkedList(expected).numeric_value()
    )

    ll_result_reverse = linked_list_summing_function(ll_b, ll_a)
    assert ll_result_reverse.values() == expected


def example():
    ll_a = LinkedList.generate(4, 0, 9)
    ll_b = LinkedList.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(sum_lists(ll_a, ll_b))


if __name__ == "__main__":
    example()
    pytest.main(args=[__file__])
