# Beautiful Triplets
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

from collections import Counter


def beautifulTriplets(d, arr):
    counts = Counter(arr)
    return sum(cnt * counts[x + d] * counts[x + 2 * d] for x, cnt in counts.items())


if __name__ == "__main__":
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(beautifulTriplets(d, arr))