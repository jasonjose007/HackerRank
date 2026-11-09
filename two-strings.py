# Two Strings
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    q = int(data[0])
    idx = 1
    out = []
    
    for _ in range(q):
        s1 = data[idx]
        s2 = data[idx+1]
        idx += 2
        
        # Two strings share a common substring of size >= 1 if and only if
        # they share at least one common character.
        set1 = set(s1)
        set2 = set(s2)
        
        if set1 & set2:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()