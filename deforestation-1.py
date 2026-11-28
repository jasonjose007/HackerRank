# Deforestation
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)

        order = []
        parent = [0] * (n + 1)
        parent[1] = -1
        stack = [1]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)

        g = [0] * (n + 1)
        for u in reversed(order):
            val = 0
            for v in adj[u]:
                if v != parent[u]:
                    val ^= (g[v] + 1)
            g[u] = val

        out.append("Alice" if g[1] != 0 else "Bob")

    print("\n".join(out))


if __name__ == "__main__":
    solve()