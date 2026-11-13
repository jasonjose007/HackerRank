# The Maximum Subarray
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def maxSubarray(arr):
    # 1. Maximum Subarray Sum (Kadane's Algorithm)
    max_so_far = arr[0]
    current_max = arr[0]
    
    # 2. Maximum Subsequence Sum
    # Sum of all positive numbers
    max_subseq = sum(x for x in arr if x > 0)
    
    # If all numbers are negative, the max subsequence sum is the maximum single element
    if max_subseq == 0:
        max_subseq = max(arr)
        
    for x in arr[1:]:
        current_max = max(x, current_max + x)
        max_so_far = max(max_so_far, current_max)
        
    return [max_so_far, max_subseq]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        arr = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        res = maxSubarray(arr)
        out.append(f"{res[0]} {res[1]}")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()