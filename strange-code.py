# Strange Counter
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def strangeCounter(t):
    rem = 3
    while t > rem:
        t -= rem
        rem *= 2
    return rem - t + 1

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        t = int(input_data[0])
        print(strangeCounter(t))

if __name__ == '__main__':
    main()