# Divisible Sum Pairs
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    ar = [int(x) for x in data[2:n+2]]
    
    count = 0
    for i in range(n):

        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
                
    print(count)

if __name__ == '__main__':
    solve()