# Counter game
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def counterGame(n):
    moves = bin(n - 1).count('1')
    return "Louise" if moves % 2 == 1 else "Richard"

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append(counterGame(n))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()