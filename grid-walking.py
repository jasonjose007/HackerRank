# Grid Walking
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    MOD = 10**9 + 7
    
    # Precompute combinations C(n, k) up to say n = 200
    MAX_M = 1005
    C = [[0] * MAX_M for _ in range(MAX_M)]
    for i in range(MAX_M):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

    idx = 0
    num_tests = int(input_data[idx])
    idx += 1
    
    out = []
    for _ in range(num_tests):
        m = int(input_data[idx])
        n = int(input_data[idx+1])
        idx += 2
        
        x = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        D = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        # ways[d][pos][steps]
        # d ranges from 0 to n-1
        # pos ranges from 1 to D[d]
        # steps ranges from 0 to m
        
        # Let's compute ways for each dimension independently:
        # W[d][steps] = number of paths of length 'steps' in dimension d starting at x[d] and staying within [1, D[d]]
        
        dim_ways = []
        for d in range(n):
            pos_limit = D[d]
            start_pos = x[d]
            
            # dp[step][position]
            # Initialize dp table
            dp = [[0] * (pos_limit + 1) for _ in range(m + 1)]
            dp[0][start_pos] = 1
            
            for step in range(m):
                for p in range(1, pos_limit + 1):
                    val = dp[step][p]
                    if val == 0:
                        continue
                    if p > 1:
                        dp[step + 1][p - 1] = (dp[step + 1][p - 1] + val) % MOD
                    if p < pos_limit:
                        dp[step + 1][p + 1] = (dp[step + 1][p + 1] + val) % MOD
            
            # Sum over all valid final positions for each number of steps
            W = [0] * (m + 1)
            for step in range(m + 1):
                W[step] = sum(dp[step]) % MOD
            dim_ways.append(W)
        
        # Now we want to distribute m total steps among n dimensions.
        # Total ways = sum over (k_0, k_1, ..., k_{n-1}) sum of k_i = m of:
        # (m! / (k_0! k_1! ... k_{n-1}!)) * product(W[d][k_d])
        
        # Since n <= 50 and m <= 1000, we can use DP to combine dimensions.
        # Let dp_combine[d][steps] be the sum of multinomial * product of ways for first d dimensions using 'steps' total steps.
        
        # To make it efficient, we can do it iteratively:
        # Start with a DP array of size m + 1 representing 0 ways for 0 steps, except 1 for 0 steps.
        # Wait, the multinomial coefficient can be built up:
        # C(m, k_0) * C(m - k_0, k_1) * ...
        
        current = [0] * (m + 1)
        current[0] = 1
        
        total_steps_used = 0
        for d in range(n):
            W = dim_ways[d]
            next_curr = [0] * (m + 1)
            # current[s] represents ways using s steps in the first d dimensions
            for s in range(total_steps_used + 1):
                if current[s] == 0:
                    continue
                # Try all possible steps k for the current dimension d
                for k in range(m - s + 1):
                    if W[k] == 0:
                        continue
                    # Multinomial coefficient factor: C(s + k, k)
                    # Wait, standard way to distribute m steps among n items:
                    # We can pick k steps for this dimension, out of remaining (m - s) steps?
                    # Actually, standard DP for multinomial coefficient:
                    # total ways = sum(k_i = m) m! / (k_0!...k_{n-1}!) * prod W_i(k_i)
                    # = sum over partitions: we can maintain current total steps s.
                    # When adding dimension d with k steps, the multiplier is C(s + k, k).
                    ways_contrib = (current[s] * W[k]) % MOD
                    ways_contrib = (ways_contrib * C[s + k][k]) % MOD
                    next_curr[s + k] = (next_curr[s + k] + ways_contrib) % MOD
            current = next_curr
            total_steps_used += m # upper bound, or just track max possible
            if total_steps_used > m:
                total_steps_used = m
                
        out.append(str(current[m]))

    print('\n'.join(out))

if __name__ == '__main__':
    solve()