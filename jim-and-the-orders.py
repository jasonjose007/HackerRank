# Jim and the Orders
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def jimOrders(orders):
    # Each customer's delivery time is the sum of their order number and preparation time.
    # We store these as tuples of (delivery_time, customer_id) to facilitate sorting.
    # customer_id is 1-indexed, corresponding to the order in which they appear in the input.
    deliveries = []
    for i in range(len(orders)):
        order_number = orders[i][0]
        prep_time = orders[i][1]
        delivery_time = order_number + prep_time
        customer_id = i + 1
        deliveries.append((delivery_time, customer_id))
    
    # Python's sort() is stable and sorts tuples lexicographically.
    # This means it sorts by delivery_time first. If delivery_times are equal,
    # it sorts by customer_id, which matches the problem's tie-breaking rule.
    deliveries.sort()
    
    # Extract the customer_ids from the sorted list of delivery tuples.
    return [d[1] for d in deliveries]

def main():
    # Read all input from standard input and split into a list of strings.
    # This handles all whitespace variations efficiently.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # The first integer is the number of customers.
    n = int(input