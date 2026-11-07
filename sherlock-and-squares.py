# Sherlock and Squares
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import math
import sys

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    return max(0, end - start + 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    q = int(data[0])
    results = []
    idx = 1
    for _ in range(q):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        results.append(str(squares(a, b)))
    print('\n'.join(results))

if __name__ == '__main__':
    main()