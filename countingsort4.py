# The Full Counting Sort
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def countSort(arr):
    n = len(arr)
    # Prepare buckets for numbers 0 to 99 (since max value is typically < 100 in this problem, but let's size it dynamically or safely to 100)
    # The max value for counting sort in this problem is usually 99.
    buckets = [[] for _ in range(100)]
    
    half_n = n // 2
    
    for i in range(n):
        val = int(arr[i][0])
        s = arr[i][1]
        if i < half_n:
            buckets[val].append('-')
        else:
            buckets[val].append(s)
            
    result = []
    for bucket in buckets:
        if bucket:
            result.extend(bucket)
            
    print(' '.join(result))

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if data:
        n = int(data[0])
        arr = []
        idx = 1
        for i in range(n):
            arr.append([data[idx], data[idx+1]])
            idx += 2
        countSort(arr)