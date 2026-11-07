# The Hurdle Race
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
    k = int(data[1])
    heights = [int(x) for x in data[2:]]
    
    max_height = max(heights)
    
    if max_height > k:
        print(max_height - k)
    else:
        print(0)

if __name__ == '__main__':
    solve()