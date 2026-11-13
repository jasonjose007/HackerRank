# Super Reduced String
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def superReducedString(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack) if stack else "Empty String"

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    result = superReducedString(s)
    print(result)