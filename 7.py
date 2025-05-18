def word_frequency(my_string: str) -> dict:
    words = my_string.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency('hello world hello'))