# Lena Sort
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


sys.setrecursionlimit(200000)

MAX_N = 100000
min_c = [0] * (MAX_N + 1)
max_c = [0] * (MAX_N + 1)


for i in range(1, MAX_N + 1):
    max_c[i] = i * (i - 1) // 2
    if i > 1:
        left = (i - 1) // 2
        right = i - 1 - left
        min_c[i] = (i - 1) + min_c[left] + min_c[right]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(q):
        n = int(input_data[idx])
        c = int(input_data[idx + 1])
        idx += 2
        
        if c < min_c[n] or c > max_c[n]:
            out.append("-1")
            continue
        
        res = []
        
        def construct(start, count, target_c):
            if count <= 0:
                return
            if count == 1:
                res.append(start)
                return
            
            c_rem = target_c - (count - 1)
            
            # Binary search for left subtree size L in [0, (count - 1) // 2]
            low = 0
            high = (count - 1) // 2
            best_l = low
            
            while low <= high:
                mid = (low + high) // 2
                rem_r = count - 1 - mid
                if min_c[mid] + min_c[rem_r] <= c_rem:
                    best_l = mid
                    # Try to see if smaller min_c (larger mid) also fits or if this is within max bounds
                    if c_rem <= max_c[mid] + max_c[rem_r]:
                        break
                    else:
                        # Need larger max_c, so smaller mid
                        high = mid - 1
                else:
                    # Need smaller min_c, so larger mid
                    low = mid + 1
            
            L = best_l
            R = count - 1 - L
            
            # Allocate comparisons
            c_l = max(min_c[L], c_rem - max_c[R])
            c_r = c_rem - c_l
            
            pivot = start + L
            res.append(pivot)
            
            construct(start, L, c_l)
            construct(pivot + 1, R, c_r)

        construct(1, n, c)
        out.append(" ".join(map(str, res)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()