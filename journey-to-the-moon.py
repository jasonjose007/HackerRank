# Journey to the Moon
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    p = int(input_data[1])
    
    parent = list(range(n))
    size = [1] * n
    
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i
    
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]

    idx = 2
    for _ in range(p):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        union(u, v)
        idx += 2
        
    total_pairs = n * (n - 1) // 2
    same_country_pairs = 0
    for i in range(n):
        if parent[i] == i:
            s = size[i]
            same_country_pairs += s * (s - 1) // 2
            
    print(total_pairs - same_country_pairs)

if __name__ == '__main__':
    solve()