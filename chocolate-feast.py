# Chocolate Feast 
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def chocolateFeast(n, c, m):
    chocolates = n // c
    total = chocolates
    wrappers = chocolates
    
    while wrappers >= m:
        new_chocolates = wrappers // m
        total += new_chocolates
        wrappers = (wrappers % m) + new_chocolates
        
    return total

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        c = int(input_data[idx+1])
        m = int(input_data[idx+2])
        idx += 3
        out.append(str(chocolateFeast(n, c, m)))
    print('\n'.join(out))

if __name__ == '__main__':
    main()