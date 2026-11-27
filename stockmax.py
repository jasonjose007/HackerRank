# Stock Maximize
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        prices = [int(x) for x in input_data[idx:idx+n]]
        idx += n
        
        profit = 0
        max_future_price = 0
        for price in reversed(prices):
            if price > max_future_price:
                max_future_price = price
            else:
                profit += max_future_price - price
        out.append(str(profit))
        
    print('\n'.join(out))

if __name__ == '__main__':
    main()