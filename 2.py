def count_occurrences(my_list: list) -> dict:
    occurrences = {}
    for num in my_list:
        occurrences[num] = occurrences.get(num, 0) + 1
    return occurrences

print(count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]))