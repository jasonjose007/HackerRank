# Alternating Characters 
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    results = []
    for i in range(1, q + 1):
        s = input_data[i]
        deletions = 0
        for j in range(len(s) - 1):
            if s[j] == s[j + 1]:
                deletions += 1
        results.append(str(deletions))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()