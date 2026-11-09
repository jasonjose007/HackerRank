# Beautiful Pairs
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys
from collections import Counter

def beautifulPairs(A, B):
    count_A = Counter(A)
    count_B = Counter(B)
    
    matching = 0
    for num in count_A:
        matching += min(count_A[num], count_B[num])
        
    if matching < len(A):
        return matching + 1
    else:
        return matching - 1

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if data:
        n = int(data[0])
        A = [int(x) for x in data[1:n+1]]
        B = [int(x) for x in data[n+1:2*n+1]]
        print(beautifulPairs(A, B))