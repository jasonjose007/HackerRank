# Marc's Cakewalk
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    total_miles = 0
    for i, c in enumerate(calorie):
        total_miles += c * (2 ** i)
    return total_miles

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    calorie = [int(x) for x in data[1:]]
    print(marcsCakewalk(calorie))

if __name__ == '__main__':
    main()