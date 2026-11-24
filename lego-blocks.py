# Lego Blocks
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    MOD = 1000000007
    MAX_M = 1000

    # Precompute P[w] for w from 0 to 1000
    P = [0] * (MAX_M + 1)
    P[0] = 1
    for i in range(1, MAX_M + 1):
        s = P[i - 1]
        if i >= 2:
            s += P[i - 2]
        if i >= 3:
            s += P[i - 3]
        if i >= 4:
            s += P[i - 4]
        P[i] = s % MOD

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2

        # Total number of ways to build a wall of height n and width w (ignoring vertical breaks)
        Total = [pow(P[i], n, MOD) for i in range(m + 1)]

        # Solid[w] is the number of valid solid walls of height n and width w
        Solid = [0] * (m + 1)
        for i in range(1, m + 1):
            sub = sum(Solid[j] * Total[i - j] for j in range(1, i)) % MOD
            Solid[i] = (Total[i] - sub) % MOD

        out.append(str(Solid[m]))

    print('\n'.join(out))

if __name__ == '__main__':
    solve()