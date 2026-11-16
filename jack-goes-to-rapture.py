# Jack goes to Rapture 
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    m = data[1]

    if n == 1:
        print(0)
        return

    end = 2 + 3 * m
    edges = [
        (w << 40) | (u << 20) | v
        for u, v, w in zip(data[2:end:3], data[3:end:3], data[4:end:3])
    ]
    edges.sort()

    parent = list(range(n + 1))
    size = [1] * (n + 1)

    for edge in edges:
        u = (edge >> 20) & 0xFFFFF
        v = edge & 0xFFFFF
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        if u != v:
            if size[u] < size[v]:
                u, v = v, u
            parent[v] = u
            size[u] += size[v]

            r1 = 1
            while parent[r1] != r1:
                parent[r1] = parent[parent[r1]]
                r1 = parent[r1]
            rn = n
            while parent[rn] != rn:
                parent[rn] = parent[parent[rn]]
                rn = parent[rn]
            if r1 == rn:
                print(edge >> 40)
                return

    print("NO PATH EXISTS")

if __name__ == "__main__":
    solve()