# Pairs
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    arr = set(int(x) for x in input_data[2:])
    
    count = 0
    for x in arr:
        if x + k in arr:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()