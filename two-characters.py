# Two Characters
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def alternate(s):
    unique_chars = list(set(s))
    max_len = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1 = unique_chars[i]
            c2 = unique_chars[j]
            
            filtered = [char for char in s if char == c1 or char == c2]
            
            is_valid = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    is_valid = False
                    break
            
            if is_valid:
                if len(filtered) > max_len:
                    max_len = len(filtered)
                    
    return max_len

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    if len(data) >= 2:
        s = data[1]
        print(alternate(s))