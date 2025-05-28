import random

def max_subarray(arr):
    if not arr:
        return 0, 0, 0

    current_sum = max_sum = arr[0]
    start_index = best_start = best_end = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            start_index = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start_index
            best_end = i

    return max_sum, best_start, best_end

def main():
    arr = [random.randint(-10,10) for _ in range(15)]
    print(f"Массив: {arr}")
    max_sum, start_idx, end_idx = max_subarray(arr)

    print(f"Искомый подмассив: {arr[start_idx:end_idx + 1]}")
    print(f"Максимальная сумма подмассива: {max_sum}")

if __name__ == "__main__":
    main()