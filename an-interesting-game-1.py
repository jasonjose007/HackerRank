# Gaming Array
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def gamingArray(arr):
    max_val = -1
    count = 0
    for x in arr:
        if x > max_val:
            max_val = x
            count += 1
            
    return "BOB" if count % 2 == 1 else "ANDY"

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    g = int(data[0])
    idx = 1
    out = []
    
    for _ in range(g):
        n = int(data[idx])
        idx += 1
        arr = [int(x) for x in data[idx:idx+n]]
        idx += n
        
        result = gamingArray(arr)
        out.append(result)
        
    print('\n'.join(out))

if __name__ == '__main__':
    main()