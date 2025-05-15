import random

def rabin_karp_search(sample : str, search_str : str) -> int:
    BASE = 256
    MOD = 10 ** 9 + 7

    power = 1
    for _ in range(len(sample) - 1):
        power = (power * BASE) % MOD

    pattern_hash = 0
    window_hash = 0
    for i in range(len(sample)):
        pattern_hash = (pattern_hash * BASE + ord(sample[i])) % MOD
        window_hash = (window_hash * BASE + ord(search_str[i])) % MOD

    for i in range(len(search_str) - len(sample) + 1):
        if pattern_hash == window_hash:
            if search_str[i:i + len(sample)] == sample:
                return i

        if i < len(search_str) - len(sample):
            window_hash = (window_hash - ord(search_str[i]) * power) % MOD
            window_hash = (window_hash * BASE + ord(search_str[i + len(sample)])) % MOD

    return -1

def use_algorithm(sample : str, search_str : str) -> int:
    return rabin_karp_search(sample, search_str)

def main():
    symb = "abcdefgh"
    corrects = list()
    for i in range(random.randint(100, 500)):
        sample = ""
        for n in range(random.randint(1, 100)):
            sample += symb[random.randint(0, len(symb) - 1)]

        search_str = ""
        for n in range(random.randint(len(sample), len(sample) * 100)):
            search_str += symb[random.randint(0, len(symb) - 1)]

        if not (use_algorithm(sample, search_str) == search_str.find(sample)):
            corrects.append((sample, search_str, use_algorithm(sample, search_str), search_str.find(sample)))

    if len(corrects) == 0:
        print("Algorithm is work correctly")
    else:
        print("Something went wrong")
        print(corrects)

if __name__ == "__main__":
    main()
