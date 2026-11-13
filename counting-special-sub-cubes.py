# Counting Special Sub-Cubes
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    q_count = int(data[0])
    idx = 1
    
    out = []
    for _ in range(q_count):
        s = int(data[idx])
        idx += 1
        cube_data = [int(x) for x in data[idx : idx + s * s * s]]
        idx += s * s * s
        
        cube = [[[0]*s for _ in range(s)] for _ in range(s)]
        for r in range(s):
            for c in range(s):
                for h in range(s):
                    cube[r][c][h] = cube_data[r * s * s + c * s + h]
        
        results = []
        for k in range(1, s + 1):
            count = 0
            # To efficiently find the maximum in all sub-cubes of size k, 
            # we can iterate over all valid starting positions (i, j, l)
            # where 0 <= i, j, l <= s - k.
            # Given constraints on s (up to usually around 10-50, let's check limits), 
            # actually s <= 50 usually. Let's write an optimized loop or DP.
            # But wait, max s is typically small for this specific problem (e.g. s <= 30 or 50).
            # Let's use a 3D sliding window or direct check if s is small.
            # Wait, 3D Sparse Table or prefix max can optimize, but for s <= 30, 
            # (s-k+1)^3 * k^3 can be large if not careful.
            # Actually, standard 3D sliding window maximum can be done in O(s^3) per k, 
            # or O(s^3) total.
            # Let's implement 3D max sliding window using monotonic queues.
            
            # Since s is at most 50, let's see:
            # For a fixed k, we need the maximum in every sub-cube of size k.
            # Using 1D sliding window max along z, then y, then x.
            
            # Let's compute max for all blocks of size k.
            # max_z[r][c][h] = max(cube[r][c][h ... h+k-1])
            max_z = [[[0]*s for _ in range(s)] for _ in range(s)]
            for r in range(s):
                for c in range(s):
                    # sliding window of size k along h
                    arr = cube[r][c]
                    # deque for sliding window max
                    from collections import deque
                    dq = deque()
                    for h in range(s):
                        while dq and dq[-1][0] <= arr[h]:
                            dq.pop()
                        dq.append((arr[h], h))
                        while dq[0][1] <= h - k:
                            dq.popleft()
                        if h >= k - 1:
                            max_z[r][c][h - k + 1] = dq[0][0]
            
            # max_zy[r][h_start][c_start] -> let's transpose for convenience
            # max_zy[r][c_start][h_start] where c_start goes up to s-k
            max_zy = [[[0]*(s - k + 1) for _ in range(s)] for _ in range(s)]
            for r in range(s):
                for h_start in range(s - k + 1):
                    arr = [max_z[r][c][h_start] for c in range(s)]
                    dq = deque()
                    for c in range(s):
                        while dq and dq[-1][0] <= arr[c]:
                            dq.pop()
                        dq.append((arr[c], c))
                        while dq[0][1] <= c - k:
                            dq.popleft()
                        if c >= k - 1:
                            max_zy[r][c - k + 1][h_start] = dq[0][0]
            
            # Now along r
            special_count = 0
            for c_start in range(s - k + 1):
                for h_start in range(s - k + 1):
                    arr = [max_zy[r][c_start][h_start] for r in range(s)]
                    dq = deque()
                    for r in range(s):
                        while dq and dq[-1][0] <= arr[r]:
                            dq.pop()
                        dq.append((arr[r], r))
                        while dq[0][1] <= r - k:
                            dq.popleft()
                        if r >= k - 1:
                            if dq[0][0] == k:
                                special_count += 1
            results.append(str(special_count))
        out.append(" ".join(results))
    
    print("\n".join(out))

if __name__ == '__main__':
    solve()