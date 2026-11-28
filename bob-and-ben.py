# Bob and Ben
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    num_games = int(next(it))
    
    results = []
    for _ in range(num_games):
        n = int(next(it))
        xor_sum = 0
        for _ in range(n):
            m = int(next(it))
            _ = next(it)  # k is not needed
            
            if m == 0 or m == 2:
                g = 0
            elif m % 2 == 1:
                g = 1
            else:
                g = 2
            
            xor_sum ^= g
            
        results.append("BOB" if xor_sum != 0 else "BEN")
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()