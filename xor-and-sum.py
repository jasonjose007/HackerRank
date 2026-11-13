# Xor and Sum
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a_str = input_data[0]
    b_str = input_data[1]

    a = int(a_str, 2)
    b = int(b_str, 2)
    
    MOD = 1000000007
    
    total_sum = 0
    for i in range(100001):
        term = (a ^ (b << i)) % MOD
        total_sum = (total_sum + term) % MOD
        
    print(total_sum)

if __name__ == '__main__':
    solve()