# Strong Password
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    has_number = any(c in numbers for c in password)
    has_lower = any(c in lower_case for c in password)
    has_upper = any(c in upper_case for c in password)
    has_special = any(c in special_characters for c in password)
    
    missing_types = 0
    if not has_number: missing_types += 1
    if not has_lower: missing_types += 1
    if not has_upper: missing_types += 1
    if not has_special: missing_types += 1
    
    return max(missing_types, 6 - n)

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    password = sys.stdin.readline().strip()
    ans = minimumNumber(n, password)
    print(ans)