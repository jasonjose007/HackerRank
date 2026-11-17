# Cavity Map
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def cavityMap(grid):
    n = len(grid)
    res = [list(row) for row in grid]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            val = grid[i][j]
            if val > grid[i-1][j] and val > grid[i+1][j] and val > grid[i][j-1] and val > grid[i][j+1]:
                res[i][j] = 'X'
    return ["".join(row) for row in res]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    grid = input_data[1:n+1]
    result = cavityMap(grid)
    for row in result:
        print(row)

if __name__ == '__main__':
    main()