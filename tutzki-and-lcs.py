# LCS Returns
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

LCS of $A[:i]$ and $B[:j]$.
    $dp2[i][j]$ is LCS of $A[i:]$ and $B[j:]$.
    $A[:i]$ is $A[0..i-1]$ (length $i$).
    $A[i:]$ is $A[i..N-1]$ (length $N-i$).
    Together $A[:i]$ and $A[i:]$ partition $A$.
    For $B$:
    We match inserted $c$ with $B[j-1]$ (1-based index $j$, so 0-based index $j-1$).
    Then $B[:j-1]$ is $B[0..j-2]$ (length $j-1$).
    $B[j:]$ is $B[j..M-1]$ (length $M-j$).
    Together $B[:j-1]$, $B[j-1]$, and $B[j:]$ partition $B$.
    So $dp1[i][j-1] = LCS(A[:i], B[:j-1])$.
    $dp2[i][j] = LCS(A[i:], B[j:])$.
    Sum = $dp1[i][j-1] + dp2[i][j]$.
    If this sum equals $L = LCS(A, B)$, then adding $c = B[j-1]$ at position