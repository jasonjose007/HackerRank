# Two Robots
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    num_test_cases = int(data[0])
    idx = 1
    
    out = []
    for _ in range(num_test_cases):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        queries = []
        for _ in range(m):
            queries.append((int(data[idx]), int(data[idx+1])))
            idx += 2
            
        # dp[i][j] represents min cost after processing i queries, 
        # where the other robot is at container j.
        # Initially, before query 1, Robot 1 is at container 1 (or functionally represented as state where other robot hasn't moved).
        # Wait, the state definition:
        # Let dp[other_pos] be the min cost such that the "other" robot is at other_pos.
        # When processing query (start, end):
        # We can either:
        # 1. Use the robot that just finished the previous query (let's call it Robot A). Its previous end was prev_end.
        #    Cost added: distance from prev_end to start + distance from start to end.
        #    The other robot stays at its position (other_pos).
        #    New state: other_pos remains the same, but the active robot's last end becomes `end`.
        # 2. Use the other robot, which was at `other_pos`.
        #    Cost added: distance from other_pos to start + distance from start to end.
        #    The robot that was active now becomes the "other" robot, and its position is the previous active robot's end (prev_end).
        #    New state: other_pos becomes prev_end, active robot ends at `end`.
        #
        # Since we process queries sequentially, we can maintain a mapping or array of `dp[j]` = min cost where the other robot is at position `j`.
        # Wait, what if no robot has moved yet?
        # We can use a virtual starting position or initialize the DP.
        # Initially, we can consider one robot is conceptually at position 1 (say, Robot 1), and Robot 2 hasn't been used yet.
        # Or even simpler:
        # Let's use a dictionary or 2D array. Since container positions are 1 to N, N <= 1000 typically, but N can be larger? 
        # Wait, constraints on N? Usually N <= 1000. Let's check typical constraints. If N is large, a dictionary is better.
        
        # Let's re-verify the state:
        # After processing i queries, one robot is at `queries[i-1][1]` (let's call its end `curr_end`), 
        # and the other robot is at some position `j` (1-indexed container).
        # Base case (before query 0):
        # We can imagine Robot 1 is at 1 (or we pay 0 distance if we use it, but wait: for the first query, if we use Robot 1 starting at 1, distance is just |start - end|? Wait!
        # Problem note: "For the first query a robot executes, there is no travel distance."
        # This means if Robot 1 is used for the first query (say from `s` to `e`), its travel distance to `s` is 0, it just moves from `s` to `e`, so cost is `|s - e|`.
        # If we use Robot 2 for the first query, its travel distance to `s` is also 0? Wait, the problem says "You have two robots that can pick up 1 piece of candy... Note: You choose which robot executes each query."
        # If Robot 2 is used for the first query, does it have to travel from somewhere? Initially, both robots are at their starting locations? 
        # Actually, standard problem interpretation for "Two Robots":
        # Initially, we can think of Robot 1 at 1 and Robot 2 at 2? No, "For the first query a robot executes, there is no travel distance."
        # This simplifies things immensely! Whichever robot executes the very first query has 0 travel distance to the start of that query.
        
        # Let's use DP where we store for each possible position of the "other" robot, the minimum total cost.
        # Actually, keeping `dp[j]` = min cost where the other robot is at container `j`, and the active robot is at `queries[i-1][1]`.
        # To avoid handling the first query specially, we can initialize:
        # Before any query, we can say Robot 1 is at `queries[0][0]` (cost 0) or just handle query 0 explicitly.
        
        s_first, e_first = queries[0]
        # First query MUST be done by one of the robots. Cost is |s_first - e_first|.
        # After first query, that robot is at `e_first`. The other robot hasn't moved yet.
        # Where is the other robot? We can consider it can be anywhere, but effectively its position doesn't matter until it's used. 
        # To fit the `dp[j]` model where `j` is the position of the other robot:
        # After query 0, active robot is at `e_first`, other robot is "not yet initialized" or at some dummy position.
        # Alternatively, using a dictionary: `dp[other_pos] = cost` where `other_pos` can be a special value `None` initially.
        
        dp = {}
        # Special key None means the other robot has not been used yet.
        dp[None] = 0
        active_end = e_first
        total_cost_so_far = abs(s_first - e_first)
        
        # Wait, if we just use dp[other_pos] representing the min cost where the inactive robot is at `other_pos` and the active robot is at `active_end`:
        # For the very first query, cost is `abs(e_first - s_first)`. Active robot is at `e_first`, other robot has `None` position.
        
        for s, e in queries[1:]:
            next_dp = {}
            
            dist_s_e = abs(s - e)
            
            for other_pos, cost in dp.items():
                # Option 1: Move the active robot (currently at active_end) to s, then to e.
                # Cost increases by abs(active_end - s) + abs(s - e).
                # The other robot remains at `other_pos`.
                # New active robot position is `e`.
                cost1 = cost + abs(active_end - s) + dist_s_e
                key1 = other_pos
                if key1 not in next_dp or cost1 < next_dp[key1]:
                    next_dp[key1] = cost1
                
                # Option 2: Move the other robot (currently at `other_pos`) to s, then to e.
                # If other_pos is None, moving it to `s` has 0 travel distance (first move for the second robot!).
                # Cost increases by: 
                # 0 if other_pos is None else abs(other_pos - s)
                # plus abs(s - e).
                # The previous active robot (at `active_end`) now becomes the "other robot".
                # New active robot position is `e`.
                # New other robot position is `active_end`.
                travel_dist = 0 if other_pos is None else abs(other_pos - s)
                cost2 = cost + travel_dist + dist_s_e
                key2 = active_end
                if key2 not in next_dp or cost2 < next_dp[key2]:
                    next_dp[key2] = cost2
                    
            dp = next_dp
            # Wait, active_end needs to be updated! 
            # But wait, in the loop above, `active_end` is a constant for the current query (it's the active end from the *previous* query).
            # Ah. If we branch, different states have different `active_end`s? 
            # No! In our state definition `dp[other_pos]`, what is the position of the active robot?
            # In the standard formulation of this problem:
            # `dp[j]` is the min cost where one robot is at `queries[i][1]` and the other robot is at `j`.
            # Notice that after query `i`, one robot is ALWAYS at `queries[i][1]`!
            # So the active robot's position is fixed to the end of the current query (`e`).
            # Therefore, we don't need to store `active_end` in the state; it's implicitly `queries[i-1][1]` for the transition into query `i`.
            
        # Let's rewrite cleanly with `dp[other_pos]` representing min cost where one robot is at `prev_e` and the other is at `other_pos`.
        
        pass


def solve_all():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    
    out = []
    for _ in range(num_test_cases):
        n = int(next(iterator))
        m = int(next(iterator))
        
        queries = []
        for _ in range(m):
            queries.append((int(next(iterator)), int(next(iterator))))
            
        # dp dictionary: key = position of the second robot (or None if second robot hasn't moved yet), 
        # value = min cost. 
        # Note that the first robot is always at the end of the previous query.
        
        # Initialize for the first query
        s0, e0 = queries[0]
        # First query costs just abs(s0 - e0) because travel to s0 is 0.
        # After query 0, robot 1 is at e0, robot 2 hasn't moved (pos = None).
        dp = {None: abs(s0 - e0)}
        prev_e = e0
        
        for s, e in queries[1:]:
            next_dp = {}
            dist = abs(s - e)
            
            for other_pos, cost in dp.items():
                # Choice A: Move robot 1 (currently at prev_e) to s, then to e.
                # Other robot stays at other_pos.
                c1 = cost + abs(prev_e - s) + dist
                if other_pos not in next_dp or c1 < next_dp[other_pos]:
                    next_dp[other_pos] = c1
                
                # Choice B: Move robot 2 (currently at other_pos) to s, then to e.
                # If other_pos is None, travel distance to s is 0.
                travel = 0 if other_pos is None else abs(other_pos - s)
                c2 = cost + travel + dist
                # Now robot 1 (at prev_e) becomes the "other robot"
                if prev_e not in next_dp or c2 < next_dp[prev_e]:
                    next_dp[prev_e] = c2
                    
            dp = next_dp
            prev_e = e
            
        out.append(str(min(dp.values())))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve_all()