def char_frequency(my_string: str) -> dict:
    s = {}
    for char in my_string:
        s[char] = s.get(char, 0) + 1
    return s

print(char_frequency('hello world'))