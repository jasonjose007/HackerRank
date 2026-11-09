# Priyanka and Toys
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def toys(w):
    w.sort()
    containers = 0
    i = 0
    n = len(w)
    while i < n:
        containers += 1
        limit = w[i] + 4
        while i < n and w[i] <= limit:
            i += 1
    return containers

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    w = [int(x) for x in input_data[1:n+1]]
    print(toys(w))

if __name__ == '__main__':
    main()