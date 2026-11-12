# Connected Cells in a Grid
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def connectedCell(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        count = 0
        
        while stack:
            curr_r, curr_c = stack.pop()
            count += 1
            
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if not visited[nr][nc] and matrix[nr][nc] == 1:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
        return count

    max_region = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                max_region = max(max_region, dfs(i, j))
                
    return max_region

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    matrix = []
    idx = 2
    for _ in range(n):
        row = [int(x) for x in data[idx:idx+m]]
        matrix.append(row)
        idx += m
        
    print(connectedCell(matrix))

if __name__ == '__main__':
    main()