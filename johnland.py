# Roads in HackerLand
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((w, u, v))
        idx += 3
        
    edges.sort()
    
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    adj = [[] for _ in range(n + 1)]
    
    for w, u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            adj[u].append((v, w))
            adj[v].append((u, w))
            parent[root_u] = root_v
            size[root_v] += size[root_u]
            size[root_u] = 0

    count = [0] * 62
    
    def dfs(u, p):
        sub_size = 1
        for v, w in adj[u]:
            if v != p:
                s = dfs(v, u)
                sub_size += s
                paths = s * (n - s)
                count[w] += paths
        return sub_size

    dfs(1, 0)

    for i in range(60):
        if count[i] > 1:
            count[i+1] += count[i] // 2
            count[i] %= 2

    max_idx = 61
    while max_idx > 0 and count[max_idx] == 0:
        max_idx -= 1
        
    res = "".join(str(count[i]) for i in range(max_idx, -1, -1))
    print(res)

if __name__ == '__main__':
    solve()