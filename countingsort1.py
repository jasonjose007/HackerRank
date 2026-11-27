# Counting Sort 1
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys


def countingSort(arr):
    freq = [0] * 100
    for x in arr:
        freq[x] += 1
    return freq


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1 : n + 1]]
    result = countingSort(arr)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()