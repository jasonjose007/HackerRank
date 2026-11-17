# Jim and the Orders
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    orders = []
    idx = 1
    for i in range(1, n + 1):
        t = int(input_data[idx])
        d = int(input_data[idx + 1])
        idx += 2
        orders.append((t + d, i))
        
    orders.sort()
    
    result = [str(customer_id) for _, customer_id in orders]
    print(' '.join(result))

if __name__ == '__main__':
    solve()