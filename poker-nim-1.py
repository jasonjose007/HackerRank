# Poker Nim
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
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        
        c = 0
        for _ in range(n):
            c ^= int(input_data[idx])
            idx += 1
            
        if c != 0:
            out.append("First")
        else:
            out.append("Second")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()