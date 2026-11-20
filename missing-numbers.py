# Missing Numbers
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys
from collections import Counter

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    m = int(input_data[n+1])
    brr = list(map(int, input_data[n+2:n+2+m]))

    count_arr = Counter(arr)
    count_brr = Counter(brr)

    missing = [x for x in count_brr if count_brr[x] > count_arr[x]]
    missing.sort()

    print(*missing)

if __name__ == '__main__':
    main()