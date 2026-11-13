# Separate the Numbers
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q_count = int(input_data[0])
    results = []
    
    for i in range(1, q_count + 1):
        s = input_data[i]
        n = len(s)
        found = False
        first_num = ""
        
        # The first number can at most be half the length of the string (plus maybe 1 for safety if it grows, but strictly <= n // 2 for 2+ numbers)
        for length in range(1, n // 2 + 1):
            sub = s[:length]
            if sub[0] == '0' and length > 1:
                break
            
            num = int(sub)
            start_num = num
            curr_str = sub
            
            while len(curr_str) < n:
                num += 1
                curr_str += str(num)
            
            if curr_str == s:
                found = True
                first_num = str(start_num)
                break
                
        if found:
            results.append(f"YES {first_num}")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()