# Jumping on the Clouds
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    n = len(c)
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if data:
        n = int(data[0])
        c = list(map(int, data[1:]))
        print(jumpingOnClouds(c))