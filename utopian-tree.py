# Utopian Tree
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def utopianTree(n):
    height = 1
    for i in range(1, n + 1):
        if i % 2 == 1:
            height *= 2
        else:
            height += 1
    return height

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    for i in range(1, t + 1):
        n = int(input_data[i])
        print(utopianTree(n))

if __name__ == '__main__':
    main()