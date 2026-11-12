# Sequence Equation
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def permutationEquation(p):
    n = len(p)
    # p is 1-indexed in the problem description, so we can pad it or adjust indices.
    # Let's use 1-based indexing for convenience.
    p = [0] + p
    
    # To find x such that p[p[x]] = i for each i from 1 to n:
    # It's easier to find where each value appears.
    # pos[val] = index where val is located in p
    pos = {}
    for index, val in enumerate(p[1:], start=1):
        pos[val] = index
        
    result = []
    for i in range(1, n + 1):
        # We need p[p[x]] = i
        # Let y = p[x], then p[y] = i.
        # So y = pos[i].
        # Then x = p[x] => x = pos[y] = pos[pos[i]].
        y = pos[i]
        x = pos[y]
        result.append(x)
        
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    p = [int(x) for x in input_data[1:]]
    
    ans = permutationEquation(p)
    for val in ans:
        print(val)

if __name__ == '__main__':
    main()