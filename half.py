# A stones game
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

restricted to $1 \le k' \le k$?
Yes, because the maximum pile size present is $N$, and the maximum bit length is $k = g(N)$.
For any $k' \le k$, there exists at least one pile with bit length $k'$, specifically $i = 2^{k'-1} \le 2^{k-1} \le N$.
So $i = 2^{k'-1}$ is ALWAYS present in the game for all $k' \in [1, k]$!
Since $k \le 62$ (for $N \le 10^{18}$), iterating $k'$ from 1 to $k$ takes at most 62 steps!

Let's dry run $N=1$:
$k = 1$.
$count = 1 - 1 + 1 = 1$ (odd).
$S = 1 \oplus 1 = 0$? Wait!
Wait! For $N=1$, $k=1$.
$count = 1$, which is odd.
$S = 1 \oplus k = 1 \oplus 1 = 0$?
WAIT!
Wait, for $N=1$:
$g(1) = 1$.
So there is ONE pile with $g=1$.
XOR sum is $g(1) = 1$!
Why did my formula give $S = 1 \oplus 1 = 0$?
Ah