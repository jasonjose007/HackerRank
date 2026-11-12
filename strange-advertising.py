# Viral Advertising
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def viralAdvertising(n):
    shared = 5
    cumulative_likes = 0
    for _ in range(n):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3
    return cumulative_likes

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    print(viralAdvertising(n))

if __name__ == '__main__':
    main()