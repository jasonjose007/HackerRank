# Save the Prisoner!
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def saveThePrisoner(n, m, s):
    return (s + m - 2) % n + 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        s = int(input_data[idx+2])
        idx += 3
        results.append(str(saveThePrisoner(n, m, s)))
    print('\n'.join(results))

if __name__ == '__main__':
    main()