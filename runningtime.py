# Running Time of Algorithms
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def runningTime(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return shifts

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if data:
        n = int(data[0])
        arr = list(map(int, data[1:]))
        result = runningTime(arr)
        print(result)