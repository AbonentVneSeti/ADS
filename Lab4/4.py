import random

def algorithm_kmp(sample : str, search_str : str) -> int:
    pi_arr = [0] * len(sample)
    j = 0
    for i in range(1, len(sample)):
        while j > 0 and sample[i] != sample[j]:
            j = pi_arr[j - 1]

        if sample[i] == sample[j]:
            j += 1
            pi_arr[i] = j


    k = 0
    l = 0
    while k < len(search_str):
        if search_str[k] == sample[l]:
            k+=1
            l+=1
            if l == len(sample):
                return k-l
        elif l == 0:
            k+=1
            if k == len(search_str):
                return -1
        else:
            l = pi_arr[l-1]

    return -1

def use_algorithm(sample : str, search_str : str) -> int:
    return algorithm_kmp(sample,search_str)

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
