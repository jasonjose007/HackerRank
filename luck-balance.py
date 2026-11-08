# Luck Balance
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def luckBalance(k, contests):
    total_luck = 0
    important = []
    
    for l, t in contests:
        if t == 0:
            total_luck += l
        else:
            important.append(l)
            
    important.sort(reverse=True)
    
    total_luck += sum(important[:k])
    total_luck -= sum(important[k:])
    
    return total_luck

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    
    contests = []
    idx = 2
    for _ in range(n):
        l = int(input_data[idx])
        t = int(input_data[idx+1])
        contests.append((l, t))
        idx += 2
        
    print(luckBalance(k, contests))

if __name__ == '__main__':
    main()