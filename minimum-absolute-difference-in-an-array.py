# Minimum Absolute Difference in an Array
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:]]
    
    arr.sort()
    
    min_diff = float('inf')
    for i in range(n - 1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            
    print(min_diff)

if __name__ == '__main__':
    solve()