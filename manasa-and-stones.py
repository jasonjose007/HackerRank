# Manasa and Stones
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    for _ in range(T):
        n = int(input_data[idx])
        a = int(input_data[idx+1])
        b = int(input_data[idx+2])
        idx += 3
        
        N = n - 1
        res = set()
        for i in range(n):
            res.add(i * a + (N - i) * b)
        
        print(*(sorted(res)))

if __name__ == '__main__':
    solve()