# The Story of a Tree
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys
import math


sys.setrecursionlimit(200000)

def solve():
    # Use a generator to read input efficiently
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    input_gen = get_input()
    
    try:
        q_str = next(input_gen)
    except StopIteration:
        return
    
    q = int(q_str)
    
    for _ in range(q):
        try:
            n = int(next(input_gen))
        except StopIteration:
            break
            
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(next(input_gen))
            v = int(next(input_gen))
            adj[u].append(v)
            adj[v].append(u)
            
        g = int(next(input_gen))
        k = int(next(input_gen))
        
        # Use a set of encoded integers for fast guess lookup
        # Encoding: u * (n + 1) + v
        guesses = set()
        for _ in range(g):
            u = int(next(input_gen))
            v = int(next(input