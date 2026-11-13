# New Year Chaos
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def minimumBribes(q):
    bribes = 0
    # Convert to 0-indexed
    q = [x - 1 for x in q]
    
    for i, person in enumerate(q):
        # person is currently at index i, original position was person
        # If a person has moved forward more than 2 positions
        if person - i > 2:
            print("Too chaotic")
            return

        # Count how many people who originally started *after* this person 
        # are currently in front of this person. 
        # Since a person can only move forward by at most 2, we only need to 
        # check from max(0, person - 1) up to i.
        for j in range(max(0, person - 1), i):
            if q[j] > person:
                bribes += 1
                
    print(bribes)

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        q = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        minimumBribes(q)

if __name__ == '__main__':
    solve()