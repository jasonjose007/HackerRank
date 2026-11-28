# Designer PDF Viewer
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    h = [int(x) for x in input_data[:26]]
    word = input_data[26]
    
    max_height = max(h[ord(char) - ord('a')] for char in word)
    area = max_height * len(word)
    print(area)

if __name__ == '__main__':
    main()