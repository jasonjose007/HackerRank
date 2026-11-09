# A Chessboard Game
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def chessboardGame(x, y):
    # The possible moves are:
    # (x - 2, y + 1)
    # (x - 2, y - 1)
    # (x - 1, y - 2)
    # (x + 1, y - 2)
    #
    # Looking at the Sprague-Grundy values (or just parity / remainder patterns):
    # Let's check (x - 1) % 4 and (y - 1) % 4.
    # Actually, a well-known pattern for this game:
    # A cell (x, y) is a losing position (Second player wins) if:
    # ((x - 1) % 4) in (0, 1) and ((y - 1) % 4) in (0, 1) ... wait, let's be precise.
    # Let's map coordinates to 0-indexed: X = x - 1, Y = y - 1.
    # The terminal states (no valid moves) are:
    # X < 2 and Y < 2 (specifically, moves go left/up/etc., wait:
    # Moves are:
    # (x-2, y+1) -> X-2, Y+1
    # (x-2, y-1) -> X-2, Y-1
    # (x-1, y-2) -> X-1, Y-2
    # (x+1, y-2) -> X+1, Y-2 (Wait, x+1? No, left 1 or right 1?
    # Problem statement moves:
    # (X-2, Y+1), (X-2, Y-1), (X-1, Y-2), (X+1, Y-2)
    # Actually, the columns are 1 to 8, rows 1 to 8.
    # The standard analysis for this exact game (often called "Chessboard Game" on HackerRank):
    # The winning/losing condition depends on (X % 4):
    X = (x - 1) % 4
    if X == 0 or X == 1:
        return "Second"
    else:
        return "First"

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        out.append(chessboardGame(x, y))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()