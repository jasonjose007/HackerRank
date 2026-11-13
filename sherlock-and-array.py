# Sherlock and Array
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    for x in arr:
        right_sum = total_sum - left_sum - x
        if left_sum == right_sum:
            return "YES"
        left_sum += x
    return "NO"

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        arr = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        out.append(balancedSums(arr))
    print('\n'.join(out))

if __name__ == '__main__':
    main()