# Highest Value Palindrome
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def highestValuePalindrome(s, n, k):
    s = list(s)
    changed = [False] * n
    
    # Step 1: Make it a palindrome using minimum changes
    left = 0
    right = n - 1
    while left < right:
        if s[left] != s[right]:
            max_char = max(s[left], s[right])
            if s[left] != max_char:
                s[left] = max_char
                changed[left] = True
            if s[right] != max_char:
                s[right] = max_char
                changed[right] = True
            k -= 1
        left += 1
        right -= 1
        
    if k < 0:
        return '-1'
        
    # Step 2: Maximize the palindrome using remaining changes
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            if k > 0 and s[left] != '9':
                s[left] = '9'
                k -= 1
        else:
            if s[left] != '9':
                if changed[left] or changed[right]:
                    if k >= 1:
                        s[left] = s[right] = '9'
                        k -= 1
                else:
                    if k >= 2:
                        s[left] = s[right] = '9'
                        k -= 2
        left += 1
        right -= 1
        
    return "".join(s)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    s = input_data[2]
    
    print(highestValuePalindrome(s, n, k))

if __name__ == '__main__':
    main()