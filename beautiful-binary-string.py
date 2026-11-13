# Beautiful Binary String
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    b = data[1]
    
    count = 0
    i = 0
    while i < n - 2:
        if b[i] == '0' and b[i+1] == '1' and b[i+2] == '0':
            count += 1
            i += 3
        else:
            i += 1
            
    print(count)

if __name__ == '__main__':
    solve()