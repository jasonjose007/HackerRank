# Lisa's Workbook
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    arr = [int(x) for x in input_data[2:]]
    
    special_count = 0
    page = 1
    
    for problems in arr:
        for p in range(1, problems + 1):
            if p == page:
                special_count += 1
            if p == problems or p % k == 0:
                page += 1
                
    print(special_count)

if __name__ == '__main__':
    solve()