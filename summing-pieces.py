# Summing Pieces
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))
    
    if n == 0:
        print(0)
        return
    
    MOD = 10**9 + 7
    
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = (pow2[i-1] * 2) % MOD
        
    total_sum = 0
    three_pow2_n_minus_1 = (3 * pow2[n-1]) % MOD
    
    for i in range(n):
        # Ci = 3 * 2^(n-1) - 2^i - 2^(n-i-1)
        ci = (three_pow2_n_minus_1 - pow2[i] - pow2[n-i-1]) % MOD
        total_sum = (total_sum + a[i] * ci) % MOD
        
    print(total_sum)

if __name__ == '__main__':
    solve()