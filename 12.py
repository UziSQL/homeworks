def list_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))

print(list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
