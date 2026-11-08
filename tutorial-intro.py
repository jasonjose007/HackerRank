# Intro to Tutorial Challenges
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def introTutorial():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    V = int(input_data[0])
    n = int(input_data[1])
    arr = [int(x) for x in input_data[2:2+n]]
    
    print(arr.index(V))

if __name__ == '__main__':
    introTutorial()