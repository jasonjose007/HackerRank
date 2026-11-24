# Append and Delete
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def appendAndDelete(s, t, k):
    common_len = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_len += 1
        else:
            break
    
    min_ops = (len(s) - common_len) + (len(t) - common_len)
    
    if k < min_ops:
        return "No"
    if (k - min_ops) % 2 == 0 or k >= len(s) + len(t):
        return "Yes"
    return "No"

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    print(appendAndDelete(s, t, k))