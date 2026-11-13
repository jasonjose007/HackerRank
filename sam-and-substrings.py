# Sam and substrings
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def substrings(n):
    MOD = 10**9 + 7
    total_sum = 0
    current_sum = 0
    
    for i, char in enumerate(n):
        digit = int(char)
        current_sum = (current_sum * 10 + digit * (i + 1)) % MOD
        total_sum = (total_sum + current_sum) % MOD
        
    return total_sum

if __name__ == '__main__':
    n = sys.stdin.readline().strip()
    if n:
        print(substrings(n))