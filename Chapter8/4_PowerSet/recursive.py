from __future__ import print_function


def subsets(arr):
    if len(arr) == 1:
        return [(), (arr[0],)]

    result = []
    n = arr[-1]

    prev = subsets(arr[:-1])
    result.extend(prev)

    for s in prev:
        result.append(tuple(list(s) + [n]))

    return result


def run(*args):
    return sorted(subsets(*args))


if __name__ == '__main__':
    q = [1, 2, 3]
    a = subsets(q)

    print('{} subsets:'.format(len(a)))
    print(a)
