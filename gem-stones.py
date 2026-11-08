# Gemstones
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def gemstones(arr):
    # Initialize the set of gemstones with the characters of the first rock
    gem_set = set(arr[0])
    
    # Intersect with the set of characters from each subsequent rock
    for rock in arr[1:]:
        gem_set.intersection_update(rock)
        
    return len(gem_set)

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        arr = input_data[1:n+1]
        print(gemstones(arr))