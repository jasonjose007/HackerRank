# Flatland Space Stations
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
    m = int(data[1])
    c = [int(x) for x in data[2:]]
    
    c.sort()
    
    max_dist = 0
    
    # Distance from the start (city 0) to the first space station
    max_dist = max(max_dist, c[0])
    
    # Distance from the end (city n-1) to the last space station
    max_dist = max(max_dist, n - 1 - c[-1])
    
    # Maximum distance between two adjacent space stations
    for i in range(1, m):
        dist = (c[i] - c[i-1]) // 2
        if dist > max_dist:
            max_dist = dist
            
    print(max_dist)

if __name__ == '__main__':
    solve()