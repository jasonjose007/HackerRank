# Mini-Max Sum
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    arr = list(map(int, sys.stdin.readline().split()))
    miniMaxSum(arr)