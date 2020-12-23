import time

from chapter_02.linked_list import LinkedList


def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll


def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll


testable_functions = (remove_dups, remove_dups_followup)
test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


def example():
    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    remove_dups(ll)
    print(ll)

    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    remove_dups_followup(ll)
    print(ll)


if __name__ == "__main__":
    example()
