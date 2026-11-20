# Migratory Birds
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    counts = [0] * 6
    for x in input_data[1:]:
        counts[int(x)] += 1
        
    max_count = 0
    ans = 1
    for bird_type in range(1, 6):
        if counts[bird_type] > max_count:
            max_count = counts[bird_type]
            ans = bird_type
            
    print(ans)

if __name__ == '__main__':
    main()