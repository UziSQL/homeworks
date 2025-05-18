def least_frequent(my_list: list) -> int:
    freq = {}
    for num in my_list:
        freq[num] = freq.get(num, 0) + 1

    least_freq_element = min(freq, key=freq.get)

    return least_freq_element

print(least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))