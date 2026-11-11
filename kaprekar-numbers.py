# Modified Kaprekar Numbers
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def kaprekarNumbers(p, q):
    kaprekar_nums = []
    for i in range(p, q + 1):
        s = str(i * i)
        d = len(str(i))
        right_part = s[-d:]
        left_part = s[:-d]
        
        right_val = int(right_part)
        left_val = int(left_part) if left_part else 0
        
        if left_val + right_val == i:
            kaprekar_nums.append(i)
            
    if kaprekar_nums:
        print(*(kaprekar_nums))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)