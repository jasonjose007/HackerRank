# Happy Ladybugs
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def happyLadybugs():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    g = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(g):
        n = int(input_data[idx])
        b = input_data[idx+1]
        idx += 2
        
        counts = {}
        has_empty = False
        for char in b:
            if char == '_':
                has_empty = True
            else:
                counts[char] = counts.get(char, 0) + 1
        
        # Check if any character has a count of 1
        possible = True
        for char, count in counts.items():
            if count == 1:
                possible = False
                break
        
        if not possible:
            out.append("NO")
            continue
            
        if has_empty:
            out.append("YES")
        else:
            # If no empty spaces, check if already happy
            happy = True
            for i in range(n):
                c = b[i]
                left_same = (i > 0 and b[i-1] == c)
                right_same = (i < n - 1 and b[i+1] == c)
                if not (left_same or right_same):
                    happy = False
                    break
            if happy:
                out.append("YES")
            else:
                out.append("NO")
                
    print('\n'.join(out))

if __name__ == '__main__':
    happyLadybugs()