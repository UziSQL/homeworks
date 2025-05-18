def missing_elements(my_list: list) -> list:
    if not my_list:
        return []
    return [num for num in range(my_list[0], my_list[-1] + 1) if num not in my_list]

print(missing_elements([1, 2, 4, 6, 7]))