# Cut the sticks
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
    arr = [int(x) for x in data[1:]]
    
    arr.sort()
    
    result = []
    result.append(len(arr))
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            result.append(n - i)
            
    for val in result:
        print(val)

if __name__ == '__main__':
    solve()