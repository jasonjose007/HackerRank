# Short Palindrome
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def shortPalindrome(s):
    MOD = 10**9 + 7
    
    # c1[a]: count of character a seen so far
    # c2[a][b]: count of pairs (a, b) seen so far
    # c3[a]: count of triples (a, x, a) seen so far
    # total: total count of valid 4-tuples (a, x, x, a)
    
    c1 = [0] * 26
    c2 = [[0] * 26 for _ in range(26)]
    c3 = [0] * 26
    total = 0
    
    for char in s:
        idx = ord(char) - ord('a')
        
        # 1. Update total 4-tuples using previous c3[idx]
        total = (total + c3[idx]) % MOD
        
        # 2. Update c3[x] for all x using current c2[x][idx]
        for i in range(26):
            c3[i] = (c3[i] + c2[i][idx]) % MOD
            
        # 3. Update c2[i][idx] for all i using current c1[i]
        for i in range(26):
            c2[i][idx] = (c2[i][idx] + c1[i]) % MOD
            
        # 4. Increment c1[idx]
        c1[idx] += 1
        
    return total

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        print(shortPalindrome(s))