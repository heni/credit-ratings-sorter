#!/usr/bin/env python3
import random

def reformat_string(rating_str):
    rating_str = rating_str.replace(
        "+", "X",
    ).replace(
        "-", "Z"
    ).replace(
        "NR", "T"
    ).replace(
        "NA", "U"
    )
    rating_str = (rating_str + "YYYY")[:4]
    return rating_str


if __name__ == "__main__":
    ratings = ["NA", "NR", "SD", "R", "D", "C", "CC", "CCC-", "CCC", "CCC+",
        "B-", "B", "B+", "BB-", "BB", "BB+", "BBB-", "BBB", "BBB+", "A-", "A", "A+",
        "AA-", "AA", "AA+", "AAA"
    ]
    random.shuffle(ratings)
    print(sorted(ratings, key=reformat_string))