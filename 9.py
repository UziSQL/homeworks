def swap_dict(d: dict) -> dict:
    swap = {}
    for key, value in d.items():
        if value not in swap:
            swap[value] = key
    return swap

print(swap_dict({1: 'a', 2: 'b', 3: 'c'}))