# Flipping the Matrix
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    q = int(data[0])
    idx = 1
    
    out = []
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        
        size = 2 * n
        matrix = []
        for _ in range(size):
            matrix.append([int(x) for x in data[idx:idx + size]])
            idx += size
            
        total_sum = 0
        for i in range(n):
            for j in range(n):
                # We can choose among 4 symmetric positions for each cell in the top-left quadrant:
                # (i, j), (i, 2n - 1 - j), (2n - 1 - i, j), (2n - 1 - i, 2n - 1 - j)
                val1 = matrix[i][j]
                val2 = matrix[i][2 * n - 1 - j]
                val3 = matrix[2 * n - 1 - i][j]
                val4 = matrix[2 * n - 1 - i][2 * n - 1 - j]
                
                total_sum += max(val1, val2, val3, val4)
                
        out.append(str(total_sum))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()