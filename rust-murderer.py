# Rust & Murderer
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
    
    output = []
    
    for _ in range(num_test_cases):
        n = int(next(iterator))
        m = int(next(iterator))
        
        main_roads = [set() for _ in range(n + 1)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            main_roads[u].add(v)
            main_roads[v].add(u)
            
        start = int(next(iterator))
        
        distances = [-1] * (n + 1)
        distances[start] = 0
        
        unvisited = set(range(1, n + 1))
        unvisited.remove(start)
        
        queue = deque([start])
        
        while queue:
            curr = queue.popleft()
            
            to_remove = []
            for neighbor in unvisited:
                if neighbor not in main_roads[curr]:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
                    to_remove.append(neighbor)
            
            for neighbor in to_remove:
                unvisited.remove(neighbor)
                
        ans = []
        for i in range(1, n + 1):
            if i != start:
                ans.append(str(distances[i]))
        output.append(" ".join(ans))
        
    print("\n".join(output))

if __name__ == '__main__':
    solve()