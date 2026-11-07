# Equalize the Array
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    
    counts = Counter(arr)
    max_freq = max(counts.values())
    
    # Minimum deletions = Total elements - Maximum frequency of any single element
    min_deletions = n - max_freq
    print(min_deletions)

if __name__ == '__main__':
    solve()