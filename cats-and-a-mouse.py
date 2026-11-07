# Cats and a Mouse
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    idx = 1
    
    output = []
    for _ in range(q):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        z = int(input_data[idx+2])
        idx += 3
        
        dist_a = abs(x - z)
        dist_b = abs(y - z)
        
        if dist_a < dist_b:
            output.append("Cat A")
        elif dist_b < dist_a:
            output.append("Cat B")
        else:
            output.append("Mouse C")
            
    print('\n'.join(output))

if __name__ == '__main__':
    solve()