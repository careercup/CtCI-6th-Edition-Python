from __future__ import print_function


def subsets(arr):
    result = [()]

    for i in range(-1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            t = []
            if i >= 0:
                t.append(arr[i])
            t.append(arr[j])

            result.append(tuple(t))

    result.append(tuple(arr))
    return result


def run(*args):
    return sorted(subsets(*args))


if __name__ == '__main__':
    q = [1, 2, 3]
    a = subsets(q)

    print('{} subsets:'.format(len(a)))
    print(a)
