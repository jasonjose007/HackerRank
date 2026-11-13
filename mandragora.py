# Mandragora Forest
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    num_queries = int(data[0])
    idx = 1
    
    out = []
    for _ in range(num_queries):
        n = int(data[idx])
        idx += 1
        h = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        h
.sort(reverse=True)
        
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + h[i]
            
        max_exp = 0
        for i in range(n + 1):
            exp = (1 + i) * suffix_sum[i]
            if exp > max_exp:
                max_exp = exp
                
        out.append(str(max_exp))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()