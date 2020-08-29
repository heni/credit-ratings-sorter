#!/usr/bin/env python3
import random
from sorter import credit_rating_sortkey


RATINGS_ORDER = ["NA", "NR", "SD", "R", "D", "C", "CC", "CCC-", "CCC", "CCC+",
    "B-", "B", "B+", "BB-", "BB", "BB+", "BBB-", "BBB", "BBB+", "A-", "A", "A+",
    "AA-", "AA", "AA+", "AAA"
]


def check_ordering():
    for _ in range(1000):
        random.seed(_)
        order = RATINGS_ORDER.copy()
        random.shuffle(order)
        order = sorted(order, key=credit_rating_sortkey)
        assert order == list(reversed(RATINGS_ORDER)), "got order: {}, expected: {}".format(
            order, list(reversed(RATINGS_ORDER)))


if __name__ == "__main__":
    check_ordering()
