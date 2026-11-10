# Larry's Array
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def larrys_array():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        A = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        inv_count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if A[i] > A[j]:
                    inv_count += 1
        
        if inv_count % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    larrys_array()