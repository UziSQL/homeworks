def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)

print(is_subset({1, 2, 3, 4, 5}, {3, 4, 5}))