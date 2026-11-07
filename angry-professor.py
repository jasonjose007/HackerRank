# Angry Professor
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
        
        on_time = 0
        for _ in range(n):
            if int(input_data[idx]) <= 0:
                on_time += 1
            idx += 1
            
        if on_time < k:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()