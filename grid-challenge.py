# Grid Challenge
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
        idx += 1
        
        grid = []
        for _ in range(n):
            row = sorted(input_data[idx])
            grid.append(row)
            idx += 1
            
        is_possible = True
        for col in range(n):
            for row in range(n - 1):
                if grid[row][col] > grid[row + 1][col]:
                    is_possible = False
                    break
            if not is_possible:
                break
                
        if is_possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()