# Ice Cream Parlor
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        m = int(input_data[idx])
        n = int(input_data[idx+1])
        idx += 2
        
        costs = []
        for i in range(n):
            costs.append(int(input_data[idx + i]))
        idx += n
        
        seen = {}
        for i, cost in enumerate(costs):
            complement = m - cost
            if complement in seen:
                out.append(f"{seen[complement] + 1} {i + 1}")
                break
            seen[cost] = i
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()