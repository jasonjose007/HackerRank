# Sales by Match
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

from collections import Counter

def sockMerchant(n, ar):
    counts = Counter(ar)
    return sum(c // 2 for c in counts.values())

if __name__ == "__main__":
    n = int(input().strip())
    ar = list(map(int, input().split()))
    print(sockMerchant(n, ar))