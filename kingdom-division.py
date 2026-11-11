# Kingdom Division
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

c$, then $w$ must be in state $(1-c, 1)$ to be satisfied by its own children.
        All these conditions are covered by the DP.

    *   Wait, what if a sibling owns *no* cities?
        The problem says "giving each of them 0 or more cities".
        If Reggie owns 0 cities, then Betty owns all $n$ cities.
        In this case, every city is Betty's.
        For each city $v$, Betty must have at least one neighbor of the same color.
        Since all cities are Betty's, this means every city $v$ must have at least one neighbor.
        In a tree with $n \ge 2$, every node has at least one neighbor.
        So if Betty owns all cities, the condition is satisfied for all cities.
        Similarly, if Reggie owns all cities, the condition is satisfied for all cities.
        Does my DP include these two cases?
        If all cities are color 0, then for every node $u$, all its children $v$ must have color 0.
        For each node $u$, $dp[u][0][1]$ would be the number of ways to color the subtree with color 0 such that $u$ is satisfied by at least one child.
        Wait, if all nodes are color 0, then $dp0[v]$ will be 0 for all $v$ except leaves.
        Let's re-trace $N=