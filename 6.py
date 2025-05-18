def unique_words(my_string: str) -> int:
    word = my_string.split()
    return len(set(word))

print(unique_words('hello world hello'))