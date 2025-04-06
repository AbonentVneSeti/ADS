import random

def boyer_moore(sample : str, search_str : str) -> int:
    n = len(search_str)
    m = len(sample)
    if m == 0:
        return 0

    # Таблица плохого символа
    bad_char = {}
    for i in range(m):
        bad_char[sample[i]] = i

    # Поиск
    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and sample[j] == search_str[shift + j]:
            j -= 1

        if j < 0:
            return shift

        else:
            shift += max(1, j - bad_char.get(search_str[shift + j], -1))

    return -1

def use_algorithm(sample : str, search_str : str) -> int:
    return boyer_moore(sample, search_str)

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