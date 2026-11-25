# Construct the Array
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def countArray(n, k, x):
    MOD = 10**9 + 7
    
    # dp0: ways to end at 1
    # dp1: ways to end at a specific value other than 1
    dp0 = 1
    dp1 = 0
    
    for _ in range(2, n + 1):
        new_dp0 = (dp1 * (k - 1)) % MOD
        new_dp1 = (dp0 + dp1 * (k - 2)) % MOD
        dp0, dp1 = new_dp0, new_dp1
        
    if x == 1:
        return dp0
    else:
        return dp1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    x = int(input_data[2])
    
    print(countArray(n, k, x))

if __name__ == '__main__':
    main()