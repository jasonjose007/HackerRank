# Candles Counting
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

            s = 0
            idx_q = h - 1
            while idx_q > 0:
                s += bit[idx_q]
                idx_q -= idx_q & -idx_q

            cnt = (s + 1) % MOD
            total_S += cnt

            # Update BIT
            idx_u = h
            while idx_u <= M:
                bit[idx_u] = (bit[idx_u] + cnt) % MOD
                cleared.append(idx_u)
                idx_u += idx_u & -idx_u

        for idx_c in cleared:
            bit[idx_c] = 0

        ans += sign * total_S

    print(ans % MOD)


if __name__ == "__main__":
    solve()

Let's double-check:
Is there any performance bottleneck?
In PyPy or CPython:
- `cleared` array can have size up to $\approx 3.2 \times 10^6 \times 16 \approx 5 \times 10^7$ if we append every `idx_u` in the update loop!
Wait! 50 million appends to `cleared` across all subsets!
That could take ~1.5 - 2 seconds just for list appends!
Can we reduce the size of `cleared`