# Password Cracker
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        passwords = list(set(data[idx:idx + n]))
        idx += n
        login_attempt = data[idx]
        idx += 1
        
        L = len(login_attempt)
        dp = [None] * (L + 1)
        dp[0] = ""
        
        for i in range(L):
            if dp[i] is None:
                continue
            for p in passwords:
                next_i = i + len(p)
                if next_i <= L and dp[next_i] is None:
                    if login_attempt.startswith(p, i):
                        dp[next_i] = p
                        
        if dp[L] is None:
            out.append("WRONG PASSWORD")
        else:
            res = []
            curr = L
            while curr > 0:
                p = dp[curr]
                res.append(p)
                curr -= len(p)
            res.reverse()
            out.append(" ".join(res))
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()