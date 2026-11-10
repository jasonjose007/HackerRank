# Count Luck
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    
    for _ in range(num_test_cases):
        n = int(next(iterator))
        m = int(next(iterator))
        grid = [next(iterator) for _ in range(n)]
        k = int(next(iterator))
        
        start = None
        end = None
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 'M':
                    start = (r, c)
                elif grid[r][c] == '*':
                    end = (r, c)
        
        # BFS to find parent pointers
        parent = {}
        queue = deque([start])
        parent[start] = None
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            curr = queue.popleft()
            if curr == end:
                break
            r, c = curr
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 'X':
                    if (nr, nc) not in parent:
                        parent[(nr, nc)] = (r, c)
                        queue.append((nr, nc))
        
        # Reconstruct path from start to end
        path = []
        curr = end
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        
        # Count wand waves
        wand_waves = 0
        for i in range(len(path) - 1):
            r, c = path[i]
            # Count valid open neighbors
            valid_neighbors = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 'X':
                    valid_neighbors += 1
            
            if i == 0:
                if valid_neighbors > 1:
                    wand_waves += 1
            else:
                # 1 neighbor is the parent, so available choices are valid_neighbors - 1
                if valid_neighbors - 1 > 1:
                    wand_waves += 1
        
        if wand_waves == k:
            print("Impressed")
        else:
            print("Oops!")

if __name__ == '__main__':
    solve()