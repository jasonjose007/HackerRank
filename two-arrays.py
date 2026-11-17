# Permuting Two Arrays
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(q):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        
        A = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        B = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        A.sort()
        B.sort(reverse=True)
        
        possible = True
        for a, b in zip(A, B):
            if a + b < k:
                possible = False
                break
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
            
    print("\n".join(results))

if __name__ == '__main__':
    solve()