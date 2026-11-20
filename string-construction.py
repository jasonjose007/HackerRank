# String Construction 
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    for i in range(1, n + 1):
        s = input_data[i]
        print(len(set(s)))

if __name__ == '__main__':
    solve()