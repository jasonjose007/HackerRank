# Counting Sort 2
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def countingSort(arr):
    # The range of numbers in this problem is typically 0 to 99 for Counting Sort 1 & 2.
    # We can create a frequency array of size 100 initialized to 0.
    freq = [0] * 100
    
    for num in arr:
        freq[num] += 1
        
    result = []
    for i in range(100):
        if freq[i] > 0:
            result.extend([i] * freq[i])
            
    return result

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if data:
        n = int(data[0])
        arr = [int(x) for x in data[1:]]
        sorted_arr = countingSort(arr)
        print(*(sorted_arr))