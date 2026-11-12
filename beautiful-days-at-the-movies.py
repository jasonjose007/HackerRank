# Beautiful Days at the Movies
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    i = int(input_data[0])
    j = int(input_data[1])
    k = int(input_data[2])

    count = 0
    for day in range(i, j + 1):
        rev = int(str(day)[::-1])
        if abs(day - rev) % k == 0:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()