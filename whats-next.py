# What's Next?
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    num_tests = int(next(it))
    
    out = []
    for _ in range(num_tests):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        
        # Array a represents alternating run-lengths, starting with 1s at even indices (0-based: 1, 0, 1, 0, ...)
        # We need the next lexicographically larger binary permutation with the same number of 1s.
        # In a binary number, to get the next greater permutation:
        # Find the rightmost '01' substring, change it to '10', and move all remaining '1's that were to the right
        # of this '01' to the far right (least significant bits).
        
        # Let's consider whether the last block is 1s or 0s.
        # If n is odd, the last block is at index n-1 (even), which represents '1's.
        # If n is even, the last block is at index n-1 (odd), which represents '0's.
        
        # Case 1: n is odd (the string ends with 1s).
        # The string ends with: ... 0^(a[n-2]) 1^(a[n-1])
        # The rightmost '01' occurs at the boundary between a[n-2] (zeros) and a[n-1] (ones).
        # Specifically, the last '0' of a[n-2] and the first '1' of a[n-1] swap.
        # That changes '... 0 1 ...' to '... 1 0 ...'.
        # The remaining 1s in a[n-1] (which is a[n-1] - 1 ones) are pushed to the very end.
        # Wait, let's trace carefully:
        # Before:
        # [prefix] [zeros: a[n-2]] [ones: a[n-1]]
        # Here, the '01' is the last zero of block n-2 and the first one of block n-1.
        # Swapping them:
        # The last zero becomes a 1.
        # That 1 joins the block before, or becomes a new 1-block. Wait!
        # The block n-2 had a[n-2] zeros. Now it has a[n-2] - 1 zeros.
        # The bit immediately after it is now 1.
        # After that bit, we have some zeros and then the remaining ones at the least significant positions.
        # How many total positions to the right of that new 1?
        # There was 1 bit (which was the first 1 of block n-1, now 0) + (a[n-1] - 1) ones.
        # Total bits after the new 1: 1 (which became 0) + (a[n-1] - 1) = a[n-1] bits.
        # To minimize the number, all ones to the right must be packed at the very end.
        # There are (a[n-1] - 1) ones.
        # So we have: 1 zero, followed by (a[n-1] - 1) ones!
        # Wait, are there any other zeros?
        # The bits after the new 1 were originally:
        # Originally: 0 1 1 1 ... 1  (one 0, then a[n-1] ones)
        # We swapped the 0 and the first 1:
        # Now we have: 1, followed by one 0 and (a[n-1] - 1) ones.
        # Can we rearrange the bits after the 1 to be smaller?
        # They are: one 0, and (a[n-1] - 1) ones.
        # The smallest arrangement of these bits is: all zeros, then all ones.
        # There is only one 0, and (a[n-1] - 1) ones!
        # So it's already one 0 followed by (a[n-1] - 1) ones!
        # Wait, what if a[n-1] == 1?
        # If a[n-1] == 1:
        # Originally: [a[n-2] zeros] [1 one]
        # Swap: [a[n-2]-1 zeros] [1 one] [1 zero]
        # Then there are 0 ones remaining.
        # So it's: [a[n-2]-1 zeros] [1 one] [1 zero].
        # What about the block before?
        # If n == 1:
        # The problem statement says: "It is guaranteed that a solution exists."
        # If n == 1, string is 111...1, no 0s, but problem says a solution exists, so n >= 2?
        # Wait, if n == 1, is it possible? "a binary number ... that is the smallest ... setCount(B) = setCount(A) and B > A".
        # If string is all 1s, B would be 10111... which has a leading 0?
        # Wait, a binary number doesn't have leading zeros. If A = "11", next is "101" (5)?
        # Does B have to have the same number of bits?
        # "Johnny wants to find a binary number, B, that is the smallest binary number B > A where setCount(B) = setCount(A)."
        # If A = 11 (3), setCount = 2. Next smallest B > A is 5 (101), setCount = 2!
        # Ah! If A is all 1s, B is 10 followed by remaining 1s!
        # Wait, does the problem guarantee a solution with arbitrary bits? "It is guaranteed that a solution exists."
        # If n = 1: A = 1^k.
        # Then B = 1 0 1^(k-1).
        # Compressed: 1 one, 1 zero, (k-1) ones.
        # Wait, if k = 1, B = 10 (2), which is 1 one, 1 zero.
        # Let's check:
        # If n == 1:
        # A has a[0] ones.
        # Next number with same set bits is: 1 followed by 0 followed by (a[0]-1) ones.
        # If a[0] == 1: 1 zero, so B = 10 -> compressed: 1 one, 1 zero -> [1, 1].
        # If a[0] > 1: B has 1 one, 1 zero, (a[0]-1) ones -> [1, 1, a[0]-1].
        # Let's check n odd > 1:
        # A ends with a[n-1] ones, preceded by a[n-2] zeros.
        # Does the rightmost '01' always occur between a[n-2] and a[n-1]?
        # YES! Because after that, there are only ones (block a[n-1]).
        # The rightmost '0' in the entire string is the last zero of block a[n-2].
        # The '1' immediately following it is the first 1 of block a[n-1].
        # So the rightmost '01' is ALWAYS this exact pair!
        # Let's verify:
        # String ends with: ... 0 (last bit of block n-2) followed by 1 1 ... 1 (a[n-1] bits).
        # We swap this '0' and the first '1':
        # The prefix up to the second-to-last 0 in block n-2 is unchanged.
        # Number of zeros remaining in block n-2: a[n-2] - 1.
        # Then the new '1' (count = 1).
        # Then the bits after this new '1' must be rearranged in increasing order (zeros then ones).
        # How many zeros were after the swapped '0'?
        # None! Because it was the last zero!
        # But wait, the swapped '0' itself is now after the new '1'!
        # So there is exactly ONE zero.
        # How many ones were after the swapped '1'?
        # Exactly a[n-1] - 1 ones.
        # So after the new '1', we have ONE zero and (a[n-1] - 1) ones!
        # Wait! The new '1' is of count 1.
        # So after block n-2 (which now has a[n-2] - 1 zeros):
        # We have:
        # - if a[n-2] - 1 > 0:
        #   block n-2 has size a[n-2] - 1 zeros.
        #   Then 1 one.
        #   Then 1 zero.
        #   Then (a[n-1] - 1) ones (if > 0).
        # - if a[n-2] - 1 == 0:
        #   Wait! If a[n-2] == 1, then a[n-2] - 1 = 0!
        #   Then the block of zeros disappears!
        #   Then the new '1' MERGES with block n-3 (which is ones)!
        #   So block n-3 becomes a[n-3] + 1 ones!
        #   Then 1 zero.
        #   Then (a[n-1] - 1) ones (if > 0).
        # Let's check Sample 0:
        # A = [4, 1, 3, 2, 4]
        # n = 5 (odd).
        # a[0]=4 (1s), a[1]=1 (0s), a[2]=3 (1s), a[3]=2 (0s), a[4]=4 (1s).
        # Here a[n-2] = a[3] = 2.
        # a[n-2] - 1 = 1 > 0.
        # So:
        # a[0..2] stays: 4, 1, 3
        # a[3] becomes: 2 - 1 = 1
        # new 1: 1
        # new 0: 1
        # remaining 1s: a[4] - 1 = 3.
        # Result: 4, 1, 3, 1, 1, 1, 3.
        # Length: 7.
        # Sample output:
        # 7
        # 4 1 3 1 1 1 3
        # Matches sample output exactly!

        # Now, what if n is even? (string ends with 0s).
        # Example: A ends with zeros.
        # [ones: a[n-3]] [zeros: a[n-2]] ... wait!
        # If n is even:
        # index n-1 is odd, so it represents ZEROS!
        # index n-2 is even, so it represents ONES!
        # index n-3 is odd, so it represents ZEROS!
        # Where is the rightmost '01'?
        # The ones are at block n-2.
        # After block n-2, there are ONLY zeros (block n-1)!
        # So there are NO ones after block n-2.
        # Therefore, the rightmost '1' in the entire string is the last bit of block n-2!
        # The rightmost '01' must use a '0' before some '1'.
        # The rightmost '0' that is immediately before a '1' is the last zero of block n-3!
        # And the '1' immediately following it is the first 1 of block n-2!
        # So the rightmost '01' is:
        # the last zero of block n-3 and the first one of block n-2!
        # Let's trace what happens when we swap them:
        # 1. Block n-3 (zeros):
        #    Its last zero becomes 1.
        #    So it has a[n-3] - 1 zeros.
        # 2. The new '1':
        #    Wait! Block n-3 had zeros. If a[n-3] - 1 == 0, it merges?
        #    Wait, if a[n-3] - 1 > 0, we have (a[n-3] - 1) zeros, then 1 one.
        #    If a[n-3] - 1 == 0, the zeros disappear, and this 1 merges with block n-4 (ones),
        #    becoming a[n-4] + 1.
        # 3. What bits are to the right of this swapped position?
        #    Originally, to the right of that '0', we had:
        #    - block n-2: a[n-2] ones. (The first one was swapped to 0).
        #      So we have one '0' (from the swap) and (a[n-2] - 1) ones.
        #    - block n-1: a[n-1] zeros.
        #    Total zeros to the right: 1 (from swap) + a[n-1] = a[n-1] + 1 zeros.
        #    Total ones to the right: a[n-2] - 1 ones.
        #    To make the number as small as possible, all zeros must come first,
        #    followed by all ones!
        #    So we have:
        #    (a[n-1] + 1) zeros,
        #    followed by (a[n-2] - 1) ones (if a[n-2] - 1 > 0).
        #
        # Wait! What is immediately after the swapped 0?
        # It became a 1!
        # Does this new 1 merge with anything?
        # To its left: block n-3 (zeros). If block n-3 had zeros left, no merge to the left.
        # To its right: all the zeros come first!
        # So to the right of the new 1, we have:
        # (a[n-1] + 1) zeros!
        # So the new 1 has count 1.
        # Wait, does the new 1 merge with block n-2?
        # No! Because block n-2's remaining ones are moved to the VERY END (after all the zeros)!
        # Let's double check this!
        # In standard next_permutation:
        # String: ... 0 1 1 1 0 0 0
        # Here:
        # block n-3 has some 0s. Last bit is 0.
        # block n-2 has a[n-2] 1s.
        # block n-1 has a[n-1] 0s.
        # The rightmost '01' is the last 0 of block n-3 and the first 1 of block n-2.
        # Swap them:
        # ... 1 0 1 1 0 0 0
        # Now, all bits after the swapped position (which is now 1) are:
        # 0, followed by (a[n-2] - 1) ones, followed by a[n-1] zeros.
        # To get next permutation, we reverse/sort the suffix in ascending order!
        # The suffix contains:
        # Number of zeros: 1 + a[n-1].
        # Number of ones: a[n-2] - 1.
        # Sorted ascending:
        # all zeros first (count = a[n-1] + 1),
        # then all ones (count = a[n-2] - 1).
        # YES! That is brilliantly simple!

        # Let's carefully trace the blocks for both cases:
        # We can implement a clean run-length encoder / merger!
        # Let's represent the prefix, then the modified parts, and then normalize (merge consecutive blocks of same bit and remove 0-length blocks).
        
        # In fact, we can represent the number as a list of (bit, count):
        # 0-th element of a is bit 1.
        # 1-st is bit 0, etc.
        # Let's build the list of (bit, count) directly!
        
        runs = []
        for i in range(n):
            bit = 1 if i % 2 == 0 else 0
            runs.append((bit, a[i]))
            
        # If n == 1:
        # runs = [(1, a[0])]
        # Next permutation:
        # We imagine a leading 0 before the number: "0" + "1"*a[0]
        # Swap 0 and first 1: "1" + "0" + "1"*(a[0]-1)
        # So new runs:
        # (1, 1), (0, 1), (1, a[0]-1)
        
        if n == 1:
            new_runs = [(1, 1), (0, 1), (1, a[0] - 1)]
        elif n % 2 == 1:
            # n is odd, ends with bit 1.
            # prefix: runs[:n-2]
            # runs[n-2] has bit 0, count a[n-2]
            # runs[n-1] has bit 1, count a[n-1]
            # After swap:
            # - runs[n-2] count becomes a[n-2] - 1
            # - new bit 1 with count 1
            # - suffix sorted:
            #   zeros: 1 (count 1)
            #   ones: a[n-1] - 1
            prefix = runs[:n-2]
            new_runs = prefix + [
                (0, a[n-2] - 1),
                (1, 1),
                (0, 1),
                (1, a[n-1] - 1)
            ]
        else:
            # n is even, ends with bit 0.
            # runs[n-3] has bit 0, count a[n-3]
            # runs[n-2] has bit 1, count a[n-2]
            # runs[n-1] has bit 0, count a[n-1]
            # prefix: runs[:n-3]
            # After swap:
            # - runs[n-3] count becomes a[n-3] - 1
            # - new bit 1 with count 1
            # - suffix sorted:
            #   zeros: a[n-1] + 1
            #   ones: a[n-2] - 1
            prefix = runs[:n-3]
            new_runs = prefix + [
                (0, a[n-3] - 1),
                (1, 1),
                (0, a[n-1] + 1),
                (1, a[n-2] - 1)
            ]
            
        # Now normalize new_runs:
        # 1. Filter out count <= 0
        # 2. Merge adjacent with same bit
        merged = []
        for bit, count in new_runs:
            if count <= 0:
                continue
            if merged and merged[-1][0] == bit:
                merged[-1] = (bit, merged[-1][1] + count)
            else:
                merged.append((bit, count))
                
        # The result must start with 1s, which it will, because:
        # If prefix was empty, new_runs starts with (0, 0) which is filtered out,
        # then (1, 1) which has bit 1!
        # So merged[0][0] is always 1.
        # The compressed array B is just the counts of merged!
        ans = [count for bit, count in merged]
        out.append(str(len(ans)))
        out.append(" ".join(map(str, ans)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()