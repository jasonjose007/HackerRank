# Prim's (MST) : Special Subtree
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys
import heapq


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((w << 16) | v)
        adj[v].append((w << 16) | u)

    start = int(next(it))

    visited = [False] * (n + 1)
    pq = [start]
    total_weight = 0
    count = 0

    while pq and count < n:
        item = heapq.heappop(pq)
        u = item & 0xFFFF
        if visited[u]:
            continue
        visited[u] = True
        total_weight += item >> 16
        count += 1
        for edge in adj[u]:
            if not visited[edge & 0xFFFF]:
                heapq.heappush(pq, edge)

    print(total_weight)


if __name__ == "__main__":
    solve()