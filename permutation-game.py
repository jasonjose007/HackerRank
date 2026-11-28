# Permutation game
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        arr = [int(x) for x in input_data[idx:idx+n]]
        idx += n
        
        # We can use memoization/DP over bitmasks.
        # State: bitmask of length n, where 1 means the element is present.
        # n <= 15, so 2^n <= 32768.
        # A state is winning if an increasing sequence is already formed?
        # The game rules:
        # "The person who played the turn that leaves an increasing sequence wins the game."
        # That means if the current player makes a move that results in an increasing sequence,
        # that player wins immediately.
        # In terms of game state:
        # From a non-increasing state mask, a player can transition to mask ^ (1 << i).
        # If the resulting mask is an increasing sequence, it's an immediate winning move.
        # Otherwise, if the next state is a losing state for the next player, then the current move is winning.
        # If no such move exists, the current state is losing.
        
        # Precompute which subsets are increasing sequences:
        # A subset of size >= 1 is increasing if the elements in order of original indices are strictly increasing.
        # Wait, size >= 1: any single element is increasing!
        # The problem statement says:
        # "The game ends when the remaining numbers form an increasing sequence of 1 or more numbers."
        # "The person who played the turn that leaves an increasing sequence wins the game."
        
        # Let's check: an array of size 1 is always increasing.
        # So whenever a player leaves 1 element, they win!
        # But players can also win earlier if they leave an increasing sequence of length >= 2.
        
        # Let is_inc[mask] be True if the subset represented by mask is an increasing sequence.
        # We can compute is_inc for each mask, or just compute DP directly.
        # Since we evaluate states from smaller popcount to larger popcount,
        # we can process masks by number of bits.
        
        memo = {}
        
        def is_increasing(mask):
            prev = -1
            for i in range(n):
                if (mask >> i) & 1:
                    if arr[i] < prev:
                        return False
                    prev = arr[i]
            return True

        # Precompute is_increasing for all masks
        is_inc = [False] * (1 << n)
        for mask in range(1, 1 << n):
            is_inc[mask] = is_increasing(mask)
            
        win = [False] * (1 << n)
        
        # For masks with popcount from 2 to n:
        # If is_inc[mask] is True, nobody is playing from this state because the game already ended when this state was reached.
        # But if we are at `mask` which is NOT increasing, the current player chooses an element to remove.
        # If removing an element leads to a mask `next_mask`:
        # - If is_inc[next_mask] is True, current player immediately wins!
        # - Else if not win[next_mask], current player wins!
        # If any such move exists, win[mask] = True, else False.
        
        # We can just iterate over mask sizes from 2 to n.
        # Sort masks by popcount or just iterate mask from 1 to (1 << n) - 1?
        # A submask has fewer bits, but iterating by bit count guarantees dependencies are met.
        
        # Actually, iterating by mask from 1 to (1 << n) - 1 does NOT guarantee smaller popcount first,
        # because mask ^ (1 << i) < mask is always true!
        # Since removing a bit always produces a strictly smaller integer (mask ^ (1 << i) < mask),
        # standard loop `for mask in range(1, 1 << n)` naturally processes all submasks before the mask!
        
        for mask in range(1, 1 << n):
            if is_inc[mask]:
                # Game is already over if someone reaches this state.
                # But as a state from which a player must move, this doesn't occur,
                # except potentially the initial state, but problem says:
                # "The permutation will not be an increasing sequence initially."
                continue
            
            can_win = False
            for i in range(n):
                if (mask >> i) & 1:
                    next_mask = mask ^ (1 << i)
                    if is_inc[next_mask] or not win[next_mask]:
                        can_win = True
                        break
            win[mask] = can_win
            
        initial_mask = (1 << n) - 1
        if win[initial_mask]:
            out.append("Alice")
        else:
            out.append("Bob")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()