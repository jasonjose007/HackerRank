# Jeanie's Route
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    
    is_target = [False] * (n + 1)
    first_target = 0
    for _ in range(k):
        c = int(next(it))
        is_target[c] = True
        first_target = c
        
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        deg[u] += 1
        deg[v] += 1
        
    removed = [False] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if deg[i] == 1 and not is_target[i]:
            q.append(i)
            
    while q:
        u = q.popleft()
        removed[u] = True
        for v, _ in adj[u]:
            if not removed[v]:
                deg[v] -= 1
                if deg[v] == 1 and not is_target[v]:
                    q.append(v)
                    
    total_w = 0
    for u in range(1, n + 1):
        if not removed[u]:
            for v, w in adj[u]:
                if u < v and not removed[v]:
                    total_w += w
                    
    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        dq = deque([start])
        far_node = start
        max_d = 0
        while dq:
            u = dq.popleft()
            d = dist[u]
            if d > max_d:
                max_d = d
                far_node = u
            for v, w in adj[u]:
                if not removed[v] and dist[v] == -1:
                    dist[v] = d + w
                    dq.append(v)
        return far_node, max_d

    a, _ = bfs(first_target)
    _, diam = bfs(a)
    print(2 * total_w - diam)

if __name__ == '__main__':
    solve()