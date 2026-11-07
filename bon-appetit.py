# Bill Division
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    bill = [int(x) for x in data[2:2+n]]
    b_charged = int(data[2+n])
    
    total_cost = sum(bill)
    anna_actual_cost = (total_cost - bill[k]) // 2
    
    if b_charged == anna_actual_cost:
        print("Bon Appetit")
    else:
        print(b_charged - anna_actual_cost)

if __name__ == '__main__':
    solve()