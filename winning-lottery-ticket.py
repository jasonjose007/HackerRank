# Winning Lottery Ticket
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def winningLotteryTicket():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    tickets = input_data[1:n+1]

    freq = [0] * 1024

    for s in tickets:
        mask = 0
        for char in s:
            mask |= 1 << (ord(char) - 48)
        freq[mask] += 1

    ans = 0
    ALL_MASK = 1023

    for i in range(1024):
        if freq[i] == 0:
            continue
        for j in range(i, 1024):
            if freq[j] == 0:
                continue
            if (i | j) == ALL_MASK:
                if i == j:
                    ans += freq[i] * (freq[i] - 1) // 2
                else:
                    ans += freq[i] * freq[j]

    print(ans)

if __name__ == '__main__':
    winningLotteryTicket()