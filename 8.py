def count_in_range(my_list: list, start: int, end: int) -> int:
    return len({num for num in my_list if start <= num <= end})

print(count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4))