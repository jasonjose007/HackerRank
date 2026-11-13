# Red John is Back
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    queries = [int(x) for x in input_data[1:t+1]]
    
    max_n = max(queries) if queries else 0
    
    # Calculate number of ways to tile a 4 x n wall.
    # Let W(n) be the number of ways to tile a 4 x n wall.
    # If we place a 4x1 brick vertically, we need to tile 4 x (n-1).
    # If we place four 1x4 bricks horizontally, they must stack to form 4x4, leaving 4 x (n-4).
    # Thus, W(n) = W(n-1) + W(n-4) for n >= 4.
    # Base cases: W(1)=1, W(2)=1, W(3)=1, W(4)=2.
    
    if max_n == 0:
        max_ways = 1
    else:
        w = [0] * (max_n + 1
)
        if max_n >= 1: w[1] = 1
        if max_n >= 2: w[2] = 1
        if max_n >= 3: w[3] = 1
        if max_n >= 4: w[4] = 2
        
        for i in range(5, max_n + 1):
            w[i] = w[i-1] + w[i-4]
            
        max_ways = max(w[1:]) if max_n >= 1 else 1

    # Sieve of Eratosthenes up to max_ways
    is_prime = [True] * (max_ways + 1)
    if max_ways >= 0:
        is_prime[0] = False
    if max_ways >= 1:
        is_prime[1] = False
        
    for p in range(2, int(max_ways**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, max_ways + 1, p):
                is_prime[i] = False
                
    # Prefix sum of primes count
    prime_count = [0] * (max_ways + 1)
    count = 0
    for i in range(max_ways + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count
        
    # Output results for each query
    out = []
    for n in queries:
        ways = w[n]
        out.append(str(prime_count[ways]))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()