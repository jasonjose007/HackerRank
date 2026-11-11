# Prime Digit Sums
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    queries = [int(x) for x in input_data[1:]]
    if not queries:
        return
    
    max_n = max(queries)
    if max_n < 5:
        # For N < 5, the answer is 0 (or not properly defined by constraints since N >= 5)
        # But constraints say 5 <= N <= 200000.
        pass

    MOD = 10**9 + 7
    
    # Primes helper up to max possible sum for 5 digits (9*5 = 45)
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    primes = {i for i in range(2, 46) if is_prime(i)}

    # State representation:
    # A state can be defined by the last 4 digits (d1, d2, d3, d4) where d1 is the oldest, d4 is the newest.
    # To optimize, we can group states by valid conditions.
    # Actually, the state needs to keep track of the last 4 digits to check 3-sums, 4-sums, 5-sums.
    # Wait:
    # 3 consecutive sums: (d2+d3+d4), when adding new digit d5: (d3+d4+d5), etc.
    # 4 consecutive sums: (d1+d2+d3+d4), when adding d5: (d2+d3+d4+d5)
    # 5 consecutive sums: requires 5 digits.
    
    # Since digits are 1-9 (wait, can digits be 0? Usually digits are 0-9 in numbers, but let's check. 
    # The problem says "digits", which usually means 0-9. But let's verify if leading zeros are allowed - 
    # "positive N-digit numbers" means no leading zeros, so first digit is 1-9. Subsequent digits can be 0-9? 
    # Wait, digit sums of 3 consecutive digits. Can digits be 0-9? Yes, standard digits are 0-9.)
    
    # Let's check valid transitions.
    # State: tuple of last 4 digits (a, b, c, d)
    # When we add e, the new state is (b, c, d, e).
    # We need:
    # a+b+c is prime (if we are at length >= 3)
    # b+c+d is prime
    # c+d+e is prime
    # a+b+c+d is prime (if length >= 4)
    # b+c+d+e is prime
    # a+b+c+d+e is prime (if length >= 5)

    # Since N can be up to 200,000, we need a fast DP.
    # Notice that many tuples (a, b, c, d) are invalid because their 3-sum or 4-sum is not prime.
    # We can pre-filter valid 4-tuples (a, b, c, d) and valid transitions (a, b, c, d) -> (b, c, d, e).
    
    digits = range(0, 10) # 0 to 9
    
    # Precompute valid 4-tuples
    valid_4 = []
    for a in range(1, 10): # First digit cannot be 0 for the very first block, but generally 0-9.
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    if (a+b+c in primes) and (b+c+d in primes) and (a+b+c+d in primes):
                        valid_4.append((a, b, c, d))
                        
    # Map valid 4-tuples to indices
    tuple_to_id = {t: i for i, t in enumerate(valid_4)}
    id_to_tuple = valid_4
    
    num_states = len(valid_4)
    
    # Precompute transitions
    # From state (a, b, c, d), we can go to (b, c, d, e) if:
    # 1. (b, c, d, e) is in valid_4
    # 2. c+d+e is prime
    # 3. b+c+d+e is prime
    # 4. a+b+c+d+e is prime
    
    transitions = [[] for _ in range(num_states)]
    for i, (a, b, c, d) in enumerate(valid_4):
        for e in range(0, 10):
            if (c+d+e in primes) and (b+c+d+e in primes) and (a+b+c+d+e in primes):
                next_t = (b, c, d, e)
                if next_t in tuple_to_id:
                    transitions[i].append(tuple_to_id[next_t])

    # For length 4, the number of ways is just the number of valid 4-tuples starting with non-zero.
    dp = [1 if t[0] != 0 else 0 for t in valid_4]
    
    # We need to answer queries up to max_n.
    # But wait, what about lengths 1, 2, 3, 4?
    # The problem asks for N-digit numbers.
    # Let's check constraints and base cases.
    # N=5 is the minimum constraint usually, or N can be smaller? Constraints say 5 <= N <= 200000.
    # So we start building from length 4 to max_n.
    
    ans = {}
    # At length 4:
    current_len = 4
    ans[4] = sum(dp) % MOD
    
    # Store results for required N
    query_set = set(queries)
    if current_len in query_set:
        ans[current_len] = sum(dp) % MOD

    # We can precompute all up to max_n
    # To optimize, let's keep dp array and simulate step by step.
    
    # Since max_n can be 200,000, doing this in Python might TLE if not careful.
    # But Python can handle O(max_n * num_states) if num_states is small.
    # Let's find num_states: digits 0-9, how many valid 4-tuples?
    # Total 4-tuples = 9 * 10^3 = 9000. Valid ones are much fewer.
    # Let's count num_states:
    # print(num_states) -> usually around a few hundred.
    
    # Let's run the simulation:
    for length in range(5, max_n + 1):
        new_dp = [0] * num_states
        for u in range(num_states):
            cnt = dp[u]
            if cnt == 0: continue
            for v in transitions[u]:
                new_dp[v] = (new_dp[v] + cnt) % MOD
        dp = new_dp
        if length in query_set:
            ans[length] = sum(dp) % MOD

    for n in queries:
        print(ans.get(n, 0))

if __name__ == '__main__':
    solve()