# Minimum Distances
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
    a = [int(x) for x in data[1:]]
    
    last_seen = {}
    min_dist = float('inf')
    
    for i, val in enumerate(a):
        if val in last_seen:
            dist = i - last_seen[val]
            if dist < min_dist:
                min_dist = dist
        last_seen[val] = i
        
    if min_dist == float('inf'):
        print(-1)
    else:
        print(min_dist)

if __name__ == '__main__':
    solve()