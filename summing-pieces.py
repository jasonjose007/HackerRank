# Summing Pieces
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

2 \times 4 = 8$.
            Value of $P_2 = 1 \times (6) = 6$.
            Total value of split = $8 + 6 = 14$.
        3.  $[1], [3, 6]$: two pieces $P_1 = [1], P_2 = [3, 6]$.
            Value of $P_1 = 1 \times (1) = 1$.
            Value of $P_2 = 2 \times (3+6) = 2 \times 9 = 18$.
            Total value of split = $1 + 18 = 19$.
        4.  $[1], [3], [6]$: three pieces $P_1 = [1], P_2 = [3], P_3 = [6]$.
            Value of $P_1 = 1 \times 1 = 1$.
            Value of $P_2 = 1 \times 3 = 3$.
            Value of $P_3 = 1 \times 6 = 6$.
            Total value of split = $1 + 3 + 6 = 10$.
        Sum of total values = $30 + 14 + 19 + 10 = 73$.
        Matches the sample output.

    *   Wait, let's re-verify the number of splits.
        For $n