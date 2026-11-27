# Tower Breakers, Again!
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    memo = {}
    
    def get_g(x):
        if x in memo:
            return memo[x]
        orig_x = x
        is_even = (x % 2 == 0)
        while x % 2 == 0:
            x //= 2
        odd_factors = 0
        d = 3
        while d * d <= x:
            while x % d == 0:
                odd_factors += 1
                x //= d
            d += 2
        if x > 1:
            odd_factors += 1
        res = odd_factors + 1 if is_even else odd_factors
        memo[orig_x] = res
        return res

    out = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        heights = input_data[idx:idx+n]
        idx += n
        
        xor_sum = 0
        for h_str in heights:
            xor_sum ^= get_g(int(h_str))
            
        if xor_sum != 0:
            out.append("1")
        else:
            out.append("2")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()