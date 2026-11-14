# The Love-Letter Mystery
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def theLoveLetterMystery(s):
    n = len(s)
    ans = 0
    for i in range(n // 2):
        ans += abs(ord(s[i]) - ord(s[n - 1 - i]))
    return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    results = []
    for i in range(1, q + 1):
        results.append(str(theLoveLetterMystery(input_data[i])))
    print('\n'.join(results))

if __name__ == '__main__':
    main()