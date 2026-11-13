# Pangrams
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def pangrams(s):
    # Convert the string to lowercase and find all unique alphabetic characters
    letters = set(c for c in s.lower() if 'a' <= c <= 'z')
    
    # If the set contains all 26 letters, it's a pangram
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    result = pangrams(s)
    print(result)