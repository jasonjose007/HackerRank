# Misère Nim
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys
from functools import reduce
import operator

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = [int(x) for x in data[idx:idx+n]]
        idx += n
        
        if max(s) == 1:
            if n % 2 == 0:
                out.append("First")
            else:
                out.append("Second")
        else:
            xor_sum = reduce(operator.xor, s, 0)
            if xor_sum != 0:
                out.append("First")
            else:
                out.append("Second")
                
    print('\n'.join(out))

if __name__ == '__main__':
    solve()