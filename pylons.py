# Goodland Electricity
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0
    
    while i < n:
        # Find the furthest possible plant location that can cover city i
        # We need a plant at index j such that j - i < k, which means j <= i + k - 1
        # Also, the plant at j must cover i, meaning j + k > i, so j >= i - k + 1
        # Since we want to cover city i, we look for the largest j in range [i - k + 1, i + k - 1] with arr[j] == 1.
        
        found = -1
        # The furthest right we can place a plant and still cover city i is min(n - 1, i + k - 1)
        # But wait, a plant at j covers cities from j - k + 1 to j + k - 1.
        # To cover city i, we need i <= j + k - 1 => j >= i - k + 1.
        # And the plant must be able to be placed, so arr[j] == 1.
        # To cover as much ground as possible to the right, we should pick the largest valid j <= i + k - 1.
        
        start = min(n - 1, i + k - 1)
        end = max(0, i - k + 1)
        
        for j in range(start, end - 1, -1):
            if arr[j] == 1:
                found = j
                break
                
        if found == -1:
            return -1
            
        plants += 1
        # This plant covers up to found + k - 1.
        # The next city that needs coverage is the first one not covered by this plant.
        # Covered up to found + k - 1, so next is found + k.
        i = found + k
        
    return plants

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    arr = [int(x) for x in input_data[2:]]
    
    print(pylons(k, arr))

if __name__ == '__main__':
    main()