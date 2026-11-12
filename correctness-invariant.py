# Correctness and the Loop Invariant
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]
        pos = i
        while pos > 0 and l[pos - 1] > value:
            l[pos] = l[pos - 1]
            pos -= 1
        l[pos] = value
    print(" ".join(map(str, l)))

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:]))
    insertion_sort(arr)

if __name__ == '__main__':
    main()