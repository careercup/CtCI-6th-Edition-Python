import collections


def count_baby_names(name_counts, synonyms):
    parent = {}
    for name in name_counts.keys():
        parent[name] = name

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x1, x2):
        r1 = find(x1)
        r2 = find(x2)
        if r1 != r2:
            parent[r1] = r2

    res = collections.defaultdict(int)
    for pair in synonyms:
        union(pair[0], pair[1])

    for key in parent.keys():
        # find root of cluster
        root = find(key)
        res[root] += name_counts[key]
    return dict(res)


test_cases = [
    # name_counts, synonyms, expected_counts
    [
        {
            "john": 10,
            "jon": 3,
            "davis": 2,
            "kari": 3,
            "johny": 11,
            "carlton": 8,
            "carleton": 2,
            "jonathan": 9,
            "carrie": 5,
        },
        [
            ("jonathan", "john"),
            ("jon", "johny"),
            ("johny", "john"),
            ("kari", "carrie"),
            ("carleton", "carlton"),
        ],
        {"john": 33, "davis": 2, "carrie": 8, "carlton": 10},
    ]
]


def test_baby_names():
    for name_counts, synonyms, expected_counts in test_cases:
        assert count_baby_names(name_counts, synonyms) == expected_counts


if __name__ == "__main__":
    test_baby_names()
