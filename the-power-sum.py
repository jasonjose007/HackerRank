# The Power Sum
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def main():
    lines = sys.stdin.read().split()
    if not lines:
        return
    X = int(lines[0])
    N = int(lines[1])
    
    dp = [0] * (X + 1)
    dp[0] = 1
    
    k = 1
    while True:
        val = k ** N
        if val > X:
            break
        for i in range(X, val - 1, -1):
            dp[i] += dp[i - val]
        k += 1
        
    print(dp[X])

if __name__ == '__main__':
    main()