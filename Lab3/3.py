import random

def build_finite_state_machine(sample : str) -> list[dict]:
    n = len(sample)
    alphabet = set(sample)
    transition_table = [{} for _ in range(n + 1)]

    for state in range(n + 1):
        for char in alphabet:
            next_state = min(n, state + 1)
            while next_state > 0 and sample[:next_state] != (sample[:state] + char)[-next_state:]:
                next_state -= 1
            transition_table[state][char] = next_state

    return transition_table

def finite_state_machine_search(sample : str, search_str : str) -> int:
    transition_table = build_finite_state_machine(sample)
    m = len(sample)
    n = len(search_str)
    state = 0

    for i in range(n):
        char = search_str[i]
        if char in transition_table[state]:
            state = transition_table[state][char]
        else:
            state = 0

        if state == m:
            return i - m + 1

    return -1

def use_algorithm(sample : str, search_str : str) -> int:
    return finite_state_machine_search(sample, search_str)

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