# Game of Stones
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print("Second" if n % 7 < 2 else "First")