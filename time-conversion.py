# Time Conversion
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys


def timeConversion(s):
    period = s[-2:]
    hh = int(s[:2])
    rest = s[2:-2]

    if period == "AM":
        if hh == 12:
            hh = 0
    else:
        if hh != 12:
            hh += 12

    return f"{hh:02d}{rest}"


if __name__ == "__main__":
    s = sys.stdin.read().strip()
    if s:
        print(timeConversion(s))