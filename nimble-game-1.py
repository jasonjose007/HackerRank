# Nimble Game
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
    out = []
    
    for _ in range(T):
        n = int(input_data[idx])
        idx += 1
        
        nim_sum = 0
        for i in range(1, n):
            c_i = int(input_data[idx + i])
            if c_i % 2 == 1:
                nim_sum ^= i
        
        idx += n
        
        if nim_sum != 0:
            out.append("First")
        else:
            out.append("Second")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()