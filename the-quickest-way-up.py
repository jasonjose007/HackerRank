# Snakes and Ladders: The Quickest Way Up
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys
from collections import deque

def quickestWayUp(ladders, snakes):
    board = {}
    for u, v in ladders:
        board[u] = v
    for u, v in snakes:
        board[u] = v

    queue = deque([(1, 0)])
    visited = {1}

    while queue:
        curr, dist = queue.popleft()
        if curr == 100:
            return dist

        for dice in range(1, 7):
            next_sq = curr + dice
            if next_sq <= 100:
                next_sq = board.get(next_sq, next_sq)
                if next_sq not in visited:
                    visited.add(next_sq)
                    queue.append((next_sq, dist + 1))
    return -1

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        ladders = []
        for _ in range(n):
            ladders.append((int(data[idx]), int(data[idx+1])))
            idx += 2
            
        m = int(data[idx])
        idx += 1
        snakes = []
        for _ in range(m):
            snakes.append((int(data[idx]), int(data[idx+1])))
            idx += 2
            
        ans = quickestWayUp(ladders, snakes)
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()