# Prime XOR
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    Q = int(input_data[0])
    idx = 1
    
    # Maximum possible XOR value given elements <= 1000 is 1023 (since 2^10 - 1 = 1023, max elements are around 1000). 
    # Actually, elements can be up to 1000, so max XOR is < 2048. Let's use 2050 as the bound.
    MAX_XOR = 2050
    
    # Precompute primes up to MAX_XOR
    is_prime = [False] * MAX_XOR
    for p in range(2, MAX_XOR):
        prime = True
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                prime = False
                break
        if prime:
            is_prime[p] = True

    MOD = 10**9 + 7

    out = []
    for _ in range(Q):
        n = int(input_data[idx])
        idx += 1
        
        # Count frequencies of each number
        freq = {}
        for _ in range(n):
            val = int(input_data[idx])
            idx += 1
            freq[val] = freq.get(val, 0) + 1
            
        # dp[v] = number of ways to form XOR sum v using processed distinct numbers
        # Initialize with ways to form 0 using empty set (1 way)
        dp = [0] * MAX_XOR
        dp[0] = 1
        
        for num, count in freq.items():
            # Number of ways to choose an even count of 'num'
            # (count // 2 + 1) choices for even numbers of 'num'
            # Number of ways to choose an odd count of 'num'
            # ((count + 1) // 2) choices for odd numbers of 'num'
            even_ways = (count // 2 + 1)
            odd_ways = ((count + 1) // 2)
            
            new_dp = [0] * MAX_XOR
            for v in range(MAX_XOR):
                if dp[v] == 0:
                    continue
                # If we pick even_ways of 'num', XOR sum doesn't change
                new_dp[v] = (new_dp[v] + dp[v] * even_ways) % MOD
                # If we pick odd_ways of 'num', XOR sum becomes v ^ num
                target = v ^ num
                new_dp[target] = (new_dp[target] + dp[v] * odd_ways) % MOD
            dp = new_dp
            
        total_valid = 0
        for p in range(2, MAX_XOR):
            if is_prime[p]:
                total_valid = (total_valid + dp[p]) % MOD
                
        out.append(str(total_valid))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()