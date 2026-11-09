# The Grid Search
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    t = int(next(iterator))
    
    out = []
    for _ in range(t):
        R = int(next(iterator))
        C = int(next(iterator))
        G = [next(iterator) for _ in range(R)]
        
        r = int(next(iterator))
        c = int(next(iterator))
        P = [next(iterator) for _ in range(r)]
        
        found = False
        # Find all occurrences of the first row of P in any row of G
        p0 = P[0]
        
        for i in range(R - r + 1):
            row = G[i]
            start_col = 0
            while True:
                idx = row.find(p0, start_col)
                if idx == -1:
                    break
                
                # Check if the rest of P matches
                match = True
                for k in range(1, r):
                    if G[i + k][idx:idx + c] != P[k]:
                        match = False
                        break
                
                if match:
                    found = True
                    break
                
                start_col = idx + 1
            
            if found:
                break
                
        if found:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()