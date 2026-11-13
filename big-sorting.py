# Big Sorting
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if not data:
        sys.exit()
    
    n = int(data[0])
    unsorted = data[1:]
    
    sorted_arr = bigSorting(unsorted)
    
    print('\n'.join(sorted_arr))