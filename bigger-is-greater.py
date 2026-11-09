# Bigger is Greater
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def next_permutation(chars):
    # Find longest non-increasing suffix
    i = len(chars) - 1
    while i > 0 and chars[i - 1] >= chars[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Let chars[i - 1] be the pivot
    # Find rightmost element that is greater than pivot
    j = len(chars) - 1
    while chars[j] <= chars[i - 1]:
        j -= 1
    
    # Swap the pivot with chars[j]
    chars[i - 1], chars[j] = chars[j], chars[i - 1]
    
    # Reverse suffix
    chars[i:] = reversed(chars[i:])
    return True

def biggerIsGreater(w):
    chars = list(w)
    if next_permutation(chars):
        return "".join(chars)
    else:
        return "no answer"

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        w = input_data[i]
        results.append(biggerIsGreater(w))
    print('\n'.join(results))

if __name__ == '__main__':
    main()