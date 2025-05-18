def most_frequent(my_list: list) -> int:
    freq = {}
    max_count = 0
    most_freq_element = None

    for num in my_list:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            most_freq_element = num

    return most_freq_element

print(most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))