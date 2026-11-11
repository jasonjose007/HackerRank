# Cut Tree
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    K = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
                
    dp = {}
    
    def dfs(u):
        if u in dp:
            return dp[u]
        
        children = [v for v in adj[u] if v != parent[u]]
        
        child_ways = []
        for v in children:
            child_ways.append(dfs(v))
            
        res = [0] * (len(children) + 1)
        res[0] = 1 
        
        for i, c_ways in enumerate(child_ways):
            next_res = [0] * len(res)
            for j in range(len(res)):
                if res[j] == 0:
                    continue
                for k, w in enumerate(c_ways):
                    if w == 0:
                        continue
                    next_res[j + k] += res[j] * w
            res = next_res
            
        final_res = [0] * (len(res) + 1)
        final_res[0] = 1
        for k in range(len(res)):
            final_res[k + 1] = res[k]
            
        dp[u] = final_res
        return final_res

    total_subtrees = 0
    for root in range(1, n + 1):
        dp.clear()
        
        parent = [0] * (n + 1)
        stack = [root]
        parent[root] = -1
        local_order = []
        
        while stack:
            u = stack.pop()
            local_order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)
                    
        def dfs_rooted(u):
            if u in dp:
                return dp[u]
            children = [v for v in adj[u] if v != parent[u]]
            child_ways = [dfs_rooted(v) for v in children]
            
            res = [0] * 1
            res[0] = 1
            
            for c_ways in child_ways:
                next_res = [0] * (len(res) + len(c_ways) - 1)
                for j in range(len(res)):
                    if res[j] == 0:
                        continue
                    for k in range(len(c_ways)):
                        if c_ways[k] == 0:
                            continue
                        next_res[j + k] += res[j] * c_ways[k]
                res = next_res
                
            final_res = [0] * (len(res) + 1)
            final_res[0] = 1
            for k in range(len(res)):
                final_res[k + 1] = res[k]
            dp[u] = final_res
            return final_res
            
        ans_poly = dfs_rooted(root)
        
        deg = [0] * (n + 1)
        for u in range(1, n + 1):
            deg[u] = len(adj[u])
            
        q = [u for u in range(1, n + 1) if deg[u] == 1 and u != root]
        if not q and n == 1:
            pass

        ways = dfs_rooted(root)
        for i in range(min(K + 1, len(ways))):
            total_subtrees += ways[i]
            
    seen = set()
    
    def count_valid_subtrees_exact(root):
        dp.clear()
        return dfs_rooted(root)

    ans = 0
    for i in range(1, n + 1):
        ways = count_valid_subtrees_exact(i)
        for k in range(1, min(K + 1, len(ways))):
            ans += ways[k]
            
    print(ans + 1)

if __name__ == '__main__':
    solve()