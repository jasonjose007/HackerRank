# Nikita and the Game
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    num_queries = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(num_queries):
        n = int(input_data[idx])
        arr = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        def get_max_score(sub_arr):
            if len(sub_arr) <= 1:
                return 0
            
            total = sum(sub_arr)
            current_sum = 0
            for i in range(len(sub_arr) - 1):
                current_sum += sub_arr[i]
                if current_sum * 2 == total:
                    left = sub_arr[:i+1]
                    right = sub_arr[i+1:]
                    return 1 + max(get_max_score(left), get_max_score(right))
            return 0

        out.append(str(get_max_score(arr)))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()