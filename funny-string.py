# Funny String
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    q = int(data[0])
    results = []
    for i in range(1, q + 1):
        s = data[i]
        n = len(s)
        funny = True
        for j in range(n - 1):
            if abs(ord(s[j+1]) - ord(s[j])) != abs(ord(s[n-1-j-1]) - ord(s[n-1-j])):
                funny = False
                break
        if funny:
            results.append("Funny")
        else:
            results.append("Not Funny")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()