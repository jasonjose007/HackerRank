# Minimum Loss
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys
import bisect

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    prices = [int(x) for x in input_data[1:]]
    
    sorted_prices = []
    min_loss = float('inf')
    
    for p in prices:
        idx = bisect.bisect_left(sorted_prices, p)
        if idx < len(sorted_prices):
            loss = sorted_prices[idx] - p
            if loss < min_loss:
                min_loss = loss
        bisect.insort(sorted_prices, p)
        
    print(min_loss)

if __name__ == '__main__':
    solve()